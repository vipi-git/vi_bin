from flask import Flask, render_template, request, send_file
import pandas as pd
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ccat.html')

@app.route('/collect_ips', methods=['POST'])
def collect_ips():
    server_list = request.form.get('server_list')
    servers = server_list.split('\n')
    
    # Define CSV file path
    csv_file = 'server_ips.csv'
    
    # Create SSH client
    #ssh = paramiko.SSHClient()
    #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Initialize CSV data
    data = []
    
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Server', 'IP Address'])
            
            for server in servers:
                server = server.strip()
                try:
                    #ssh.connect(server)
                    #_, stdout, _ = ssh.exec_command('hostname -I')
                    #ip_address = stdout.read().decode().strip()
                    ip_address = "192.168.1.1"
                    csv_writer.writerow([server, ip_address])
                except Exception as e:
                    print(f"Error connecting to {server}: {str(e)}")
                #finally:
                    #ssh.close()
    
        return send_file(csv_file, as_attachment=True)
    
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
