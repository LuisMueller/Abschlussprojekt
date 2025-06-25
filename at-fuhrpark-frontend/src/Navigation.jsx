import atLogo from './assets/logo.png'
import './App.css'

function Navigation(){
    return (
        <nav>
            <div>
                <img src = {atLogo} />
            </div>
            <div>
                <a href="https://www.alexanderthamm.com/de/">Homepage</a>
            </div>
            <div>
                <a href="https://alexander-thamm-gmbh.app.personio.com/">Personio</a>
            </div>
            <div>
                <a href="https://athamm.sharepoint.com/_layouts/15/sharepoint.aspx">Sharepoint</a>
            </div>
            <div>
                <a href="https://www.alexanderthamm.com/de/">Support</a>
            </div>
        </nav>
    )
}
export default Navigation