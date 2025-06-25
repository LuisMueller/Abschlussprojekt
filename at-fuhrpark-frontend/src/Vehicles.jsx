import { useState } from 'react'
import { vehicles } from './config.js'
import vehicle1BMW from './assets/1erBMW.jpg'
import vehicle3BMW from './assets/3erBMW.jpg'
import vehicleVKlasse from './assets/VKlasse.jpg'

const vehicleimages = {
    1: vehicle1BMW,
    2: vehicle3BMW,
    3: vehicleVKlasse

}

function Vehicles ({ unavailableVehicleIds, setClickedVehicleId }) {

    const onClickVehicle = vehicle => {
        if (!unavailableVehicleIds.includes(vehicle.id))
            setClickedVehicleId(vehicle.id)
    }

    return (
        <div className="vehicles">
            {vehicles.map(vehicle => (
                <div
                    key={vehicle.id}
                    className={'item ' + (unavailableVehicleIds.includes(vehicle.id) ? 'unavailable' : '')}
                >
                    <p>{vehicle.model}</p>
                    <img
                        src={vehicleimages[vehicle.id]}
                        alt={vehicle.model}
                        className={'img'}
                    />
                    <p>Seats: {vehicle.seats}</p>
                    <p>Location: {vehicle.location}</p>
                    <p>Verbrauch: {vehicle.verbrauch}</p>

                    <button onClick={_ => onClickVehicle(vehicle)} className={'bookbtn'}>Book</button>
                </div>
            ))}

        </div>
    )
}
export default Vehicles