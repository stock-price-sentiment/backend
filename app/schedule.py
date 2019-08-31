import datetime
import functools
import logging
import time
import threading

class Scheduler(object):
  def __init__(self):
    self.tasks = [];
  
  def run_pending(self):
    """Run all tasks that are scheduled to run.
    Please note that it is *intended behavior that tick() does not
    run missed jobs*. For example, if you've registered a job that
    should run every minute and you only call tick() in one hour
    increments then your job won't be run 60 times in between but
    only once.
    """
    runnable_tasks = (task for task in self.tasks if task.should_run)
    for task in sorted(runnable_tasks):
        task.run()

  def run_continuously(self, interval=1):
      cease_continuous_run = threading.Event()

      class ScheduleThread(threading.Thread):
          @classmethod
          def run(cls):
              while not cease_continuous_run.is_set():
                  self.run_pending()
                  time.sleep(interval)

      continuous_thread = ScheduleThread()
      continuous_thread.start()
      return cease_continuous_run

  def run_all(self, delay_seconds=0):
      """Run all jobs regardless if they are scheduled to run or not.
      A delay of `delay` seconds is added between each job. This helps
      distribute system load generated by the jobs more evenly
      over time."""
      logger.info('Running *all* %i jobs with %is delay inbetween',
                  len(self.jobs), delay_seconds)
      for task in self.tasks:
          task.run()
          time.sleep(delay_seconds)

  def clear(self):
      """Deletes all scheduled jobs."""
      del self.tasks[:]

  def every(self, interval=1):
      """Schedule a new periodic job."""
      task = Task(interval)
      self.tasks.append(task)
      return task

  @property
  def next_run(self):
      """Datetime when the next job should run."""
      return min(self.tasks).next_run

  @property
  def idle_seconds(self):
      """Number of seconds until `next_run`."""
      return (self.next_run - datetime.datetime.now()).total_seconds()
