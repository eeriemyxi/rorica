import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import ThemeSwitcher from './ThemeSwitcher.tsx'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Rorica</h1>
      <p>This is a client for <label class="rorica-text">Rorica</label>, a chat app.</p>
      <ThemeSwitcher/>
    </>
  )
}

export default App
