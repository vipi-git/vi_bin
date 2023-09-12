from flask import Flask, render_template, request, send_file, jsonify, Response
import requests
import csv
import time

app = Flask(__name__)

CHEF_AUTOMATE_URL = 'https://your-chef-automate-url/api/v0'  # Replace with your Chef Automate URL

# A dictionary to store the status for each server
server_status = {}

@app.route('/')
def index():
    return render_template('ccat2.html')

@app.route('/collect_ips', methods=['POST'])
def collect_ips():
    server_list = request.form.get('server_list')
    servers = server_list.split('\n')
    
    # Define CSV file path
    csv_file = 'server_ips.csv'
    
    # Initialize CSV data
    data = []
    
    headers = {
        'Content-Type': 'application/json',
        'api-token': 'your-api-token'  # Replace with your Chef Automate API token
    }
    
    def generate():
        for server in servers:
            server = server.strip()
            try:
                #response = requests.get(f'{CHEF_AUTOMATE_URL}/nodes/{server}', headers=headers)
                #if response.status_code == 200:
                #    node_data = response.json()
                ip_address = "192.168.1.1"
                data.append([server, ip_address])
                server_status[server] = f'Success: {ip_address}'
            except Exception as e:
                data.append([server, str(e)])
                server_status[server] = str(e)
            
            yield "data: {}\n\n".format(server_status[server])
            time.sleep(0.1)  # Add a small delay for demonstration purposes
            
        with open(csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Server', 'IP Address'])
            csv_writer.writerows(data)
    
    return Response(generate(), content_type='text/event-stream')

@app.route('/download_csv')
def download_csv():
    return send_file('server_ips.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
