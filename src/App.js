import logo from './logo.svg';
import { BsBell } from 'react-icons/bs'
import './App.css';

function testprint(){
  console.log('button pressed');
  fetch('http://192.168.4.1:8000');
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <BsBell className='resized' onClick={testprint}/>
        {/* <img onClick={testprint} src={BsBell}  alt="logo" /> */}
        <p>
          Press the button above to ring the bell.
        </p>
      </header>
    </div>
  );
}

export default App;
