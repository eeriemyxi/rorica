import ThemeSwitcher from './ThemeSwitcher.tsx'
import './App.css'

function App() {
  return (
    <>
      <h1>Rorica</h1>
      <p>This is a client for <label className="rorica-text">Rorica</label>, a chat app.</p>
      <ThemeSwitcher/>
    </>
  )
}

export default App
