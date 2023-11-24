# travel_info

Scrapes https://tfgm.com/ travel info and produce a page for display on tvs. Currently configured for displays on 1080p tv in portrait mode.

Source urls are scraped for the table containing the timetable. A page is generated with each timetable, javascript rotates through each one. CSS used to hide or format the columns of the table. 

Changes to layout/tags of the source pages may cause layout issues or stop page displaying anything.

## Install
 - Setup a virtual env
 - install requirements.txt
 - Setup webserver to serve static directory
 - Add cronjob to run process.py at desired interval

 Config
 Add a settings.py file with sources in the following format. The provided settings_example.py can be renamed and used.
 <code>
 SOURCES = [
    {
        'url': 'url for page with timetable',
        'table_id': 'id of table containing timetable',
        'name': 'Name to be displayed'
    },
]
</code>

## Development
Change the template files then run process.py to see changes. 
Edit and complile SCSS to make changes to CSS.
npm install -g sass
sass styles.scss > styles.css