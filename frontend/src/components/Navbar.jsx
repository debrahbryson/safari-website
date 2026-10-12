import { Link, NavLink } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/" className="brand">
        <span className="brand-icon">🦁</span> Serengeti Trails
      </Link>
      <div className="nav-links">
        <NavLink to="/" end>Home</NavLink>
        <NavLink to="/tours">Safaris</NavLink>
        <a href="#contact">Contact</a>
      </div>
    </nav>
  )
}
