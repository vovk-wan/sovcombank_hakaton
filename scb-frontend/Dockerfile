FROM node:19-alpine as build
WORKDIR /frontend
COPY package.json package-lock.json ./
RUN npm install -g @angular/cli
RUN npm install
COPY . .
RUN npm run build

#STAGE 2
FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build /frontend/dist/admindashboard /usr/share/nginx/html


#COPY nginx.conf /etc/nginx/conf.d
