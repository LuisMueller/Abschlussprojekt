import { useState } from 'react'
import { BACKEND_URL, vehicles  } from './config.js'
import vehicle1BMW from './assets/1erBMW.png'
import vehicle5BMW from './assets/5erBMW.png'
import vehicleVKlasse from './assets/VKlasse.png'

const vehicleimages = {
    1: vehicle1BMW,
    2: vehicle5BMW,
    3: vehicleVKlasse

}

function Buchen({ vehicleId, date, endDate, passengers, setClickedVehicleId }) {
    const [destination, setDestination] = useState('')
    const [reason, setReason] = useState('')

    const buchen = async e => {
        e.preventDefault()
        const rs = await fetch(`${BACKEND_URL}/buchung`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id: 1,
                vehicle_id: vehicleId,
                start: date,
                end: endDate,
                destination: destination,
                reason: reason
            }),
        })
        const json = await rs.json()

        if (rs.status !== 200)
            return alert(json.detail)

        setClickedVehicleId(null)
    }

    const vehicle = vehicles.find(v => v.id === vehicleId)

    const dateToString = date => {
        return `${date.getDate()}.${date.getMonth()+1}.${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}`
    }

    return (
        <form className='booking' onSubmit={buchen}>
            <h1>Booking</h1>
            <p>{dateToString(date)} to {dateToString(endDate)}</p>
            <p>{vehicles.filter(v => v.id === vehicleId).at(0).model}</p>
            <p>Location: {vehicle.location}</p>
            <p>Seats: {vehicle.seats}</p>
            <p>Fuel consumption: {vehicle.verbrauch}</p>
            <p>Power: {vehicle.leistung} </p>
            <p>Boot capacity: {vehicle.kofferraumvolumen}</p>

            <div>
                <p>Destination</p>
                <input
                    value={destination}
                    onChange={e => setDestination(e.target.value)}
                />
            </div>
            <div>
                <p>Reason</p>
                <input
                    value={reason}
                    onChange={e => setReason(e.target.value)}
                />
            </div>
            <div className='booking-img-container'>
                <img
                    src={vehicleimages[vehicle.id]}
                    alt={vehicle.model}
                    className= 'img'
                />
            </div>
            <input
                type='submit'
                value='Book'
                style={{
                    position: 'relative',
                    top: '-650px',
                    width: '30%',
                    height: '10%',
                    margin: '2rem auto 3rem 0%',
                    cursor: 'pointer',
                    backgroundColor: 'rgb(255,121,43)',
                    border: 'none',
                    color: 'black',
                    fontSize: '1.5rem'
                }}
            />
        </form>
    );
}
export default Buchen