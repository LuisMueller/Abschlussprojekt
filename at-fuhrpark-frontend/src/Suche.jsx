import { useState } from 'react'
import { BACKEND_URL, vehicles } from './config.js'
import Vehicles from './Vehicles.jsx'
import Buchen from './Buchen.jsx'
import BookingsList from './BuchungsListe.jsx'

function Suche(){
    const stdEndDate = new Date()
    stdEndDate.setDate(stdEndDate.getDate() + 1)

    const [date, setDate] = useState(new Date())
    const [endDate, setEndDate] = useState(stdEndDate)
    const [passanger, setPassanger] = useState(1)
    const [unavailableVehicleIds, setUnavailableVehicleIds] = useState([])

    const [clickedVehicleId, setClickedVehicleId] = useState(null)

    const search = async (e) => {
        e.preventDefault()

        if (endDate < date)
            alert('Enddate is before stardate')

        const rs = await fetch(BACKEND_URL + '/buchung/filter?start=' + date.toISOString() + '&end=' + endDate.toISOString() + '&limit=10&offset=0', {
            method: 'Get',
        })
        const buchungen = await rs.json()
        const arr = []
        for (const buchung of buchungen) {
            arr.push(buchung.vehicle_id)
        }
        for (const vehicle of vehicles) {
            if (vehicle.seats < passanger)
                arr.push(vehicle.id)
        }
        setUnavailableVehicleIds(arr)
    }

    return (
        <main>
            <p>Booking of Alexander Thamm</p>
            <form className="search" onSubmit={search}>
                <div>
                    <p>Start date</p>
                    <input
                        type="datetime-local"
                        value={date.toISOString().slice(0, 16)}
                        onChange={e => setDate(new Date(e.target.value))}
                    />
                </div>
                <div>
                    <p>End date</p>
                    <input
                        type="datetime-local"
                        value={endDate.toISOString().slice(0, 16)}
                        onChange={e => setEndDate(new Date(e.target.value))}
                    />
                </div>
                <div>
                    <p>Passenger</p>
                    <input
                        type="number"
                        min={1}
                        value={passanger}
                        onChange={e => setPassanger(parseInt(e.target.value || 1))}
                    />
                </div>
                <input
                    type="submit"
                    value={"Suchen"}
                />
            </form>
            <Vehicles
                unavailableVehicleIds={unavailableVehicleIds}
                setClickedVehicleId={setClickedVehicleId}
            />
            {clickedVehicleId != null && (
                <div className="modal-container" onClick={e => e.target.className.includes('modal-container') && setClickedVehicleId(null)}>
                    <div className="modal">
                        <Buchen
                            vehicleId={clickedVehicleId}
                            date={date}
                            endDate={endDate}
                            passengers={passanger}
                            setClickedVehicleId={setClickedVehicleId}
                        />
                    </div>
                </div>
            )}

        </main>
    )
}

export default Suche