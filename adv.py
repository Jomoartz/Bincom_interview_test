import sqlite3
import webbrowser
import os
def generate_html(content, content1):
    html_content = """
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Bincom test</title>
            <meta name='author' dcontent= 'MOGBOLU JOHN-JOHANAN'>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body class="container-fluid">
            <p>question 1</p>
            <p> {0} </p>
            
            <p>question 2</p>
            <p> {1}</p>
            <script><script>
        </body>
    </html>
 """.format(content, content1)
    return html_content




result = ''
pu_results = ''
#table: states
#table: lga
#table:party
#table: ward
#table: announced_pu_results
#table: announced_ward_results
#table: announced_lga_results
#table: agentname
#table: polling_unit
#table: announced_state_results

def main():
    conn = sqlite3.connect('./data.sqlite.sql')

    cursor = conn.cursor()

    random_polling_u_id = '8'

    cursor.execute('SELECT *  FROM announced_pu_results where polling_unit_uniqueid=?', (random_polling_u_id,))
    content = cursor.fetchall()
    result = f"{content[0] [2]}:{content[0] [3]}, {content[1] [2]}:{content[1] [3]}, {content[2] [2]}:{content[2] [3]}, {content[3] [2]}:{content[3] [3]}, {content[4] [2]}:{content[4] [3]}, {content[5] [2]}:{content[5] [3]}"

    cursor.execute('SELECT *  FROM announced_pu_results')
    pu_content = cursor.fetchall()


    #Take data from pu_results according to the respective parties
    
    pu_results = {}
    for data in pu_content:
                
        if pu_results.get(data[2]) != None:
            pu_results[data[2]] = int(data[3]) + pu_results[data[2]]
            print('1 works')
        else:
            pu_results[data[2]] = int(data[3])
            print('2 works')

    conn.close()

    total_lga_results = f"PDP:{pu_results['PDP']}, DPP:{pu_results['DPP']}, ACN:{pu_results['ACN']}, PPA:{pu_results['PPA']}, CDC:{pu_results['CDC']}, JP:{pu_results['JP']}, ANPP:{pu_results['ANPP']}, LABO:{pu_results['LABO']}, CPP:{pu_results['CPP']}"

    if content:
        html_content = generate_html(result, total_lga_results)

    else:
        html_content = "<p> content for id: {} not found</p>".format(random_polling_u_id,)
    file_path = os.path.join(os.getcwd(), 'result.html')
    with open(file_path, 'w') as file:
        file.write(html_content)


    webbrowser.open('file://' + file_path)

if __name__== '__main__':
    main()