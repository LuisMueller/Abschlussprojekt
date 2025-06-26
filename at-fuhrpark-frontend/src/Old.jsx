import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function Old() {
    const [count, setcount] = useState(3)
    const increaseCount = () => {
        setcount(count + 1)
        localStorage.setItem('count', count + 1)
    }

    useEffect(() => {
        const oldCount = parseInt(localStorage.getItem('count'))
        setcount(oldCount)
    }, [])

    return (
        <>
            <p>Counter {count}</p>
            <button onClick={increaseCount}>Press</button>
        </>
    )
}

//export default App
