from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
import os
# Create your views here.

def main(request):
    return HttpResponse('This main page')

def home(request):
    return redirect('main')  #This will redirect to main upon typing the /home

def about(request):
    return HttpResponse('This about page')

def months(request,month):
    if month.lower() == 'favicon.ico':
        return HttpResponse("")
    dir={

    "January": "The year kicks off with January, symbolizing new beginnings. It’s named after Janus, the Roman god of doors and transitions, reflecting the duality of looking back and forward. Special days include New Year’s Day and celebrations like Makar Sankranti and Pongal in India. The cold winter weather in many parts makes it a cozy time for reflection and resolutions.",
    
    "February": "The shortest month, February is packed with charm. Known for Valentine's Day, it's a month of love and togetherness. In the Northern Hemisphere, winter begins to ease. Festivals like Maha Shivaratri and Chinese New Year sometimes occur in this month, adding cultural richness.",
    
    "March": "March welcomes spring, a season of renewal and growth. Named after Mars, the Roman god of war, it's a time for blooming flowers and pleasant weather. Key events include International Women’s Day and Holi in India. It’s also when the Spring Equinox occurs, balancing day and night.",
    
    "April": "April bursts with life, with nature in full bloom. Often associated with rebirth and renewal, it’s famous for April Fool's Day and Earth Day. The month also marks significant festivals like Easter and Ram Navami. Its name derives from the Latin 'aperire,' meaning 'to open,' symbolic of spring’s flourishing.",
    
    "May": "A month of warmth and vitality, May is named after Maia, the Greek goddess of growth. It’s the time for Labor Day celebrations and honoring mothers on Mother's Day. In India, Buddha Purnima and summer vacations bring joy and relaxation to many.",
    
    "June": "June ushers in summer with long, sunlit days. It’s named after Juno, the Roman goddess of marriage and childbirth. World Environment Day and Father’s Day are notable celebrations, while the Summer Solstice marks the year’s longest day in the Northern Hemisphere.",
    
    "July": "Named after Julius Caesar, July is synonymous with summer fun, picnics, and barbecues. In the US, Independence Day celebrations dominate the month, while in India, the monsoon rains often bring relief. It’s also a time for leisure and mid-year reflections.",
    
    "August": "August, named after Emperor Augustus, exudes grandeur. In India, it’s marked by Independence Day and Raksha Bandhan. Globally, the Perseid meteor shower graces the skies. With monsoons continuing in many regions, it’s a mix of celebrations and natural beauty.",
    
    "September": "The transition month of September bridges summer and fall. The Autumn Equinox marks a balance of day and night. Key days include Teacher’s Day in India and International Literacy Day. Its name stems from the Latin 'septem,' meaning seven, as it was the seventh month in the ancient Roman calendar.",
    
    "October": "October dazzles with autumn hues and festive fervor. Dussehra and Diwali in India light up the month, while Halloween adds spookiness in the West. The crisp air and falling leaves create a picturesque setting. It’s also a time to reflect on gratitude and change.",
    
    "November": "November is a blend of serenity and festivity. In India, Diwali sometimes falls in this month, and Gurpurab is celebrated with devotion. Globally, Thanksgiving in the US promotes family bonds and gratitude. The cooler weather and shorter days make it a time for cozy gatherings.",
    
    "December": "December, the year’s finale, is synonymous with celebrations. Christmas and New Year’s Eve dominate the month, spreading joy and togetherness. In India, winter begins in full swing, and various cultural festivities abound. It’s a reflective time, embracing both nostalgia and hope for the future."
    }
    month_details={
        'name':month.capitalize(),
        'des': dir[month.capitalize()]
    }
    
    return render(request,'Optical_main/month.html',{'month_data':month_details})

    