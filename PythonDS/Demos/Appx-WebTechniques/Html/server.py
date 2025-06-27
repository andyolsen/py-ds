from http.server import BaseHTTPRequestHandler, HTTPServer
import pandas as pd

df = pd.read_csv('BergenWeather2019.csv', 
                  parse_dates=['MonthYear'], 
                  date_format='%m/%Y')

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        
        try:
            with open('index.html') as file:
                html_page = file.read()

            html_table = df.to_html(index=False)
            html_page = html_page.replace("DATA", html_table)
            print(html_page)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(html_page.encode('utf-8'))
            
        except IOError:
            self.send_error(500, 'Server error occurred')
     
server = HTTPServer(('', 8000), MyHandler)
print('Web server listening on http://localhost:8000/')
server.serve_forever()