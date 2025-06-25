import Navigation from './Navigation.jsx'
import Suche from './Suche.jsx'
import BuchungsListe from './BuchungsListe.jsx'
import React from 'react';
import './App.css';

function App(){
    return (
        <>
            <Navigation></Navigation>
            <Suche></Suche>
            <section className="hero-background"></section>
            <BuchungsListe></BuchungsListe>
        </>
    )
}

export default App