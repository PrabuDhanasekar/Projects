# # Horoscope
from random import *
star = input("What is your star sign: ")
star = star.lower()
# Aries Leo Sagittarius Cancer Scorpio Pisces Taurus Virgo Gemini Libra Aquarius Capricorn

benefits = ["Today is a day for action! Take charge and make things happen.",
            "Relax and indulge in some self-care. You've earned it!",
            "Embrace your curiosity and try something new today.",
            "Spend time with loved ones and nurture your relationships.",
            "Your confidence is shining bright. Use it to inspire others.",
            "Stay organized and focused. Your hard work will pay off.",
            "Balance is key today. Take time to find harmony in your life.",
            "Your passion is your power. Channel it into something creative.",
            "Adventure is calling! Explore and expand your horizons.",
            "Set your goals high and work steadily towards them.",
            "Think outside the box and embrace your originality.",
            "Let your imagination run wild. Creativity is your strength"]

ran = choice(benefits)

match star:
    case "aries":
        print(ran)

    case "leo":
        print(ran)

    case "sagittarius":
        print(ran)

    case "cancer":
        print(ran)

    case "scorpio":
        print(ran)

    case "pisces":
        print(ran)

    case "taurus":
        print(ran)

    case "virgo":
        print(ran)
    
    case "gemini":
        print(ran)
    
    case "libra":
        print(ran)

    case "aquarius":
        print(ran)

    case "capricorn":
        print(ran)
    
    case _:
        print("Oops! That doesn't seem to be a valid star sign. Please try again")