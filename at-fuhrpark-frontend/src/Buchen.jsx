import { useState } from 'react'
import { BACKEND_URL, vehicles  } from './config.js'
import vehicle1BMW from './assets/1erBMW.jpg'
import vehicle3BMW from './assets/3erBMW.jpg'
import vehicleVKlasse from './assets/VKlasse.jpg'

const vehicleimages = {
    1: vehicle1BMW,
    2: vehicle3BMW,
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

    const dateToString = date => {
        return `${date.getDate()}.${date.getMonth()+1}.${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}`
    }

    return (
        <form className="booking" onSubmit={buchen}>
            <h2>Booking</h2>
            <p>{dateToString(date)} to {dateToString(endDate)}</p>
            <p>{vehicles.filter(v => v.id === vehicleId).at(0).model}</p>
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
            <div>
                <img
                    src={vehicleimages[vehicles.id]}
                    alt={vehicles.model}
                    className={'img'}
                />
            </div>
            <input
                type="submit"
            />
        </form>
    );
}
export default Buchen