from datetime import timedelta

def semana(date):
    start = date - timedelta( days=date.weekday() )
    end = start + timedelta( days=6 )
    sem = str(start)+ " a " + str(end)
    return(sem)