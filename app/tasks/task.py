class Task(object):
    """A periodic task as used by `Scheduler`."""
    def __init__(self, interval):
        self.interval = interval  # pause interval * unit between runs
        self.job_func = None  # the job job_func to run
        self.unit = None  # time units, e.g. 'minutes', 'hours', ...
        self.at_time = None  # optional time at which this job runs
        self.last_run = None  # datetime of the last run
        self.next_run = None  # datetime of the next run
        self.period = None  # timedelta between runs, only valid for

    def __lt__(self, other):
        """PeriodicTasks are sortable based on the scheduled time
        they run next."""
        return self.next_run < other.next_run

    def __repr__(self):
        def format_time(t):
            return t.strftime("%Y-%m-%d %H:%M:%S") if t else '[never]'

        timestats = '(last run: %s, next run: %s)' % (
                    format_time(self.last_run), format_time(self.next_run))

        job_func_name = self.job_func.__name__
        args = [repr(x) for x in self.job_func.args]
        kwargs = ['%s=%s' % (k, repr(v))
                  for k, v in self.job_func.keywords.items()]
        call_repr = job_func_name + '(' + ', '.join(args + kwargs) + ')'

        if self.at_time is not None:
            return 'Every %s %s at %s do %s %s' % (
                   self.interval,
                   self.unit[:-1] if self.interval == 1 else self.unit,
                   self.at_time, call_repr, timestats)
        else:
            return 'Every %s %s do %s %s' % (
                   self.interval,
                   self.unit[:-1] if self.interval == 1 else self.unit,
                   call_repr, timestats)

    @property
    def second(self):
        assert self.interval == 1
        return self.seconds

    @property
    def seconds(self):
        self.unit = 'seconds'
        return self

    @property
    def minute(self):
        assert self.interval == 1
        return self.minutes

    @property
    def minutes(self):
        self.unit = 'minutes'
        return self

    @property
    def hour(self):
        assert self.interval == 1
        return self.hours

    @property
    def hours(self):
        self.unit = 'hours'
        return self

    @property
    def day(self):
        assert self.interval == 1
        return self.days

    @property
    def days(self):
        self.unit = 'days'
        return self

    @property
    def week(self):
        assert self.interval == 1
        return self.weeks

    @property
    def weeks(self):
        self.unit = 'weeks'
        return self

    def at(self, time_str):
        """Schedule the task every day at a specific time.
        Calling this is only valid for tasks scheduled to run every
        N day(s).
        """
        assert self.unit == 'days'
        hour, minute = [int(t) for t in time_str.split(':')]
        assert 0 <= hour <= 23
        assert 0 <= minute <= 59
        self.at_time = datetime.time(hour, minute)
        return self

    def do(self, job_func, *args, **kwargs):
        """Specifies the job_func that should be called every time the
        job runs.
        Any additional arguments are passed on to job_func when
        the job runs.
        """
        self.job_func = functools.partial(job_func, *args, **kwargs)
        functools.update_wrapper(self.job_func, job_func)
        self._schedule_next_run()
        return self

    @property
    def should_run(self):
        """True if the job should be run now."""
        return datetime.datetime.now() >= self.next_run

    def run(self):
        """Run the task and immediately reschedule it."""
        logger.info('Running task %s', self)
        self.job_func()
        self.last_run = datetime.datetime.now()
        self._schedule_next_run()

    def _schedule_next_run(self):
        """Compute the instant when this task should run next."""
        # Allow *, ** magic temporarily:
        # pylint: disable=W0142
        assert self.unit in ('seconds', 'minutes', 'hours', 'days', 'weeks')
        self.period = datetime.timedelta(**{self.unit: self.interval})
        self.next_run = datetime.datetime.now() + self.period
        if self.at_time:
            assert self.unit == 'days'
            self.next_run = self.next_run.replace(hour=self.at_time.hour,
                                                  minute=self.at_time.minute,
                                                  second=self.at_time.second,
                                                  microsecond=0)
            # If we are running for the first time, make sure we run
            # at the specified time *today* as well
            if (not self.last_run and
                    self.at_time > datetime.datetime.now().time()):
                self.next_run = self.next_run - datetime.timedelta(days=1)
