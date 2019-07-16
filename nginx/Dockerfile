# retrieve the latest nginx image.
FROM nginx

# remove the default config file.
RUN rm /etc/nginx/conf.d/default.conf

# copy our config file over to the docker container.
COPY nginx.conf /etc/nginx/conf.d/