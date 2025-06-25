import { useState, useEffect } from 'react'
import { BACKEND_URL, vehicles } from './config.js'

function BuchungsListe() {
  const [bookings, setBookings] = useState([])

  useEffect(() => {
    const fetchBookings = async () => {
      const now = new Date()
      const future = new Date()
      future.setFullYear(future.getFullYear() + 1)

      const qs = new URLSearchParams({
        start:  now.toISOString(),
        end:    future.toISOString(),
        limit:  '10',
        offset: '0',
      })

      const res = await fetch(`${BACKEND_URL}/buchung/filter?${qs}`, {
        method: 'GET',
      })
      const data = await res.json()
      setBookings(data)
    }

    fetchBookings()
  }, [])
      const handleDelete = async bookingId => {
        if (!window.confirm('Soll diese Buchung wirklich gelöscht werden?')) return

        try {
          const res = await fetch(`${BACKEND_URL}/buchung/${bookingId}`, {
            method: 'DELETE',               // DELETE-Route aufrufen
          })
          if (!res.ok) {
            const err = await res.json()
            alert(err.detail || 'Löschen fehlgeschlagen')
            return
          }
          setBookings(prev => prev.filter(b => b.booking_id !== bookingId))
        } catch (e) {
          alert('Fehler beim Löschen: ' + e.message)
        }
      }

  if (bookings.length === 0) {
    return <p>Keine aktuellen oder anstehenden Buchungen.</p>
  }

return (
    <div className="buchungs-liste">
      <h2>Aktuelle &amp; kommende Buchungen</h2>
      <ul>
        {bookings.map(b => {
          const vehicle = vehicles.find(v => v.id === b.vehicle_id)
          return (
            <li
              key={b.booking_id}
              className="buchungs-item"
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center'
              }}
            >
              <div>
                <strong>
                  {vehicle?.model ?? `Fzg #${b.vehicle_id}`}
                </strong>{' '}
                von{' '}
                {new Date(b.bookingstart).toLocaleString().slice(0, 16)}
                {' '}bis{' '}
                {new Date(b.bookingend).toLocaleString().slice(0, 16)}
                {b.passenger_count != null && (
                  <> · Passagiere: {b.passenger_count}</>
                )}
              </div>

              <button
                onClick={() => handleDelete(b.booking_id)}
                style={{ marginLeft: '1rem', marginRight: '33px', borderRadius: '8px', border: '1px solid rgb(255, 121, 43)'}}
              >
                Löschen
              </button>
            </li>
          )
        })}
      </ul>
    </div>
  )
}

export default BuchungsListe
