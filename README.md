# day59_100

# Blog Post Website
This project is a simple blog post website built using Flask, HTML, CSS, and JavaScript. The website displays a series of posts with titles, subtitles, and images. Users can navigate through different posts to read their content.

## Features
- __Dynamic Content Display:__ The website dynamically displays blog posts, each with a title, subtitle, image, and body text.
- __Responsive Design:__ Utilizes Bootstrap for a responsive and mobile-friendly design.
- __Navigation:__ Easy navigation with a navbar linking to the Home, About, and Contact pages.
- __Template Rendering:__ Utilizes Flask's Jinja2 templating engine to render pages dynamically.

![](https://github.com/AlvinChin1608/day59_100/blob/main/gif_demo/ScreenRecording2024-07-25at16.55.18-ezgif.com-video-to-gif-converter.gif)

## Project Structure
```python
.
├── static
│   ├── css
│   │   └── styles.css
│   ├── js
│   │   └── scripts.js
│   └── assets
│       └── favicon.ico
├── templates
│   ├── layout.html
│   ├── post.html
│   ├── about.html
│   ├── contact.html
│   └── index.html
├── app.py
└── README.md
```
- static/css/styles.css: Contains custom CSS styles.
- static/js/scripts.js: Includes JavaScript for interactive elements.
- templates/layout.html: The base layout for all pages, including header and footer.
- templates/post.html: Template for displaying individual blog posts.
- main.py: The main application file that handles routes and logic.
