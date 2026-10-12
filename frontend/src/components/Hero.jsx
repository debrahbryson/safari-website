import { Link } from 'react-router-dom'

export default function Hero() {
  return (
    <section className="hero">
      <div className="hero-overlay" />
      <div className="hero-content">
        <p className="hero-eyebrow">Tanzania · East Africa</p>
        <h1>The Wild Is Calling.<br />Answer It.</h1>
        <p className="hero-sub">
          Handcrafted safaris across the Serengeti, Ngorongoro Crater and beyond —
          led by expert guides, built around you.
        </p>
        <div className="hero-actions">
          <Link to="/tours" className="btn btn-primary">Explore Safaris</Link>
          <a href="#why-us" className="btn btn-ghost">Why Travel With Us</a>
        </div>
      </div>
    </section>
  )
}
