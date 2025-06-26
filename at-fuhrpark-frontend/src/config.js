//insert production URL after Server setup
export const BACKEND_URL = !import.meta.env.PROD? 'http://localhost:8000' : ''

export const vehicles = [
    {
        id : 1,
        model: '1er BMW',
        location: 'München',
        seats: 4,
        verbrauch: '6,5 l/100 km',
        leistung: '122 PS',
        kofferraumvolumen: '380 l'
    },
    {
        id: 2,
        model: '5er BMW',
        location: 'München',
        seats: 5,
        verbrauch: '6,5 l/100 km',
        leistung: '208 PS',
        kofferraumvolumen: '410 l'

    },
    {
        id: 3,
        model: 'Mercedes VKlasse',
        location: 'München',
        seats: 7,
        verbrauch: '7,1 l/100 km',
        leistung: '163 PS',
        kofferraumvolumen: '1030 l'
    },
]
