from datetime import datetime as _dt

def _create_generator(file_handler, threshold):
    
    row2list = lambda row: row.strip().split(",")
    
    for line in file_handler:
        try:
            if int(row2list(line)[3]) >= threshold:
                yield row2list(line)
        except ValueError as message:
            print("Header found, ValueError:", message)
            yield row2list(line)
        
def get_revenue_date(file_path, revenue_threshold, dayOfTheWeek=False):
    #row2list = lambda row: row.strip().split(",")
    with open(file_path, "r") as marketing_data:
        #marketing_generator = (row2list(line) for line in marketing_data if int(row2list(line)[3]) >= revenue_threshold)
        marketing_generator = _create_generator(marketing_data, revenue_threshold)
        
        open('Marketing_filtered_data.csv', "w").close()
            
        with open('Marketing_filtered_data.csv', 'a') as file_handler:
            for row in marketing_generator:
                date, day_name, visitors, revenue, marketing_spend, promo = row
                
                try:
                    date = _dt.strptime(date, '%d/%m/%Y')
                    date = date.strftime("%d-%m-%Y")
                except ValueError as message:
                    date = date
                
                date_string = day_name if dayOfTheWeek else date
                #print(f"{date_string},{revenue}", file=file_handler)
                print(",".join([date_string, revenue]), file=file_handler)