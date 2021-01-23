from datetime import datetime
from datetime import timedelta

class DaysCalculator():
    
    dataAtual = datetime
    dataInicio = datetime
    diasUteis = int
    dataFim = datetime

    def calculate(self,horas=int):

        self.dataAtual = datetime.now()
        self.dataInicio = self.dataAtual + timedelta(days= 7 - self.dataAtual.weekday() if self.dataAtual.weekday()>3 else 1)
        self.diasUteis = int
        self.dataFim = self.dataInicio

        if (horas >= 20):

            self.diasUteis = horas / 2
        else:

            self.diasUteis = horas
        
        self.diasUteis = int(self.diasUteis)

        for dias in range(self.diasUteis - 1):

            self.dataFim += timedelta(days= 7 - self.dataFim.weekday() if self.dataFim.weekday()>3 else 1)

        return [self.dataInicio.strftime('%d-%m-%Y'),self.dataFim.strftime('%d-%m-%Y')]