# Vue 3 + Vite + Flask + T/JS 

This template should help get you started developing with Flask, Vue 3 and T/JScript in Vite, with Hot Module Replacement support. The template serves as the base that you can build from and modify to your needs.

## How to get started

1. Clone this repo.
2. Delete the `.git` folder and `git init` yours in the project folder.
3. Run `npm install` to install the dependencies.
4. Profit!

## How to use in Development

1. Run the flask server `flask run` or `python app.py`.
2. Run Vite dev server `npm run dev`.
3. Open Vite server's localhost in your browser.
4. Flask routes are served under `/api`. So go to `http://localhost:5173/api/` for Flask's rendered templates. (*Port used differs*)

## How to use in Build

1. Build the project using `npm run build`.
2. Change `MODE` in `.env` to `MODE=production`
3. Run flask server and open it in your browser.





### What's happening here?

Basically, for HMR to work, static files like JS, CSS, etc.. need to be served from Vite's server, while api requests are handled by flask's server. So here, you have two options. Either you use flask server and proxy requests for static files to Vite, or use Vite's server and proxy api requests to flask server (which is what I've done here, [as in React](https://create-react-app.dev/docs/proxying-api-requests-in-development/)).

Your specific use cases might be a bit different, that's why I wanted to keep the config changes to a minimum. So you could alter it to fit your specific needs.
