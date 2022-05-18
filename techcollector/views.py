from django.shortcuts import render
from django.http import HttpResponse

class Tech:
  def __init__(self, name, type, specs, price):
    self.name = name
    self.type = type
    self.specs = specs
    self.price = price

techs = [
  Tech('Radeon 5700xt', 'Graphics Card', '8GB 256-Bit GDDR6, Core Clock 1770 MHzBoost Clock 2010 MHz, 2 x HDMI 2 x DisplayPort 1.4, 2560 Stream Processors, PCI Express 4.0 x16', 650),
  Tech('Intel i9 12900k', 'Computer Processor', 'Max turbo Frequency : 6 Cores, 5.20ghz, Total L2 cache : 12 mb, Max Turbo Power : 241 w', 700),
  Tech('Noctua NH-D15', 'CPU Air Cooler', ' 6 HeatPipes dual tower design, 2x NF-A154 140mm fans with PWM, Color:Brown(Ugly af)', 100)
]


# Create your views here.
def home(request):
    return render(request,'home.html', {'techs':techs})

def tech(request):
    return render(request,'tech.html',)