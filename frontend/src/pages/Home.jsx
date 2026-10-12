import { useEffect, useState } from 'react'
import Hero from '../components/Hero'
import TourCard from '../components/TourCard'
import { getTours } from '../api'

const WHY = [
  { icon: '🧭', title: 'Local Expert Guides', text: 'Born-and-raised Tanzanian guides with 10+ years tracking the migration.' },
  { icon: '🛻', title: 'Private 4x4 Vehicles', text: 'Pop-up roof Land Cruisers with charging ports, fridges and binoculars.' },
  { icon: '🌿', title: 'Responsible Travel', text: 'Fair wages, community partnerships and low-impact eco-lodges.' },
  { icon: '💬', title: '24/7 Support', text: 'WhatsApp support from the moment you land at Kilimanjaro Airport.' },
]

export default function Home() {
  const [featured, setFeatured] = useState([])
  useEffect(() => { getTours().then(r => setFeatured(r.data.slice(0, 3))).catch(() => {}) }, [])

  return (
    <>
      <Hero />
      <section className="section" id="why-us">
        <h2 className="section-title">Why Travel With Us</h2>
        <div className="why-grid">
          {WHY.map(w => (
            <div className="why-card" key={w.title}>
              <span className="why-icon">{w.icon}</span>
              <h3>{w.title}</h3>
              <p>{w.text}</p>
            </div>
          ))}
        </div>
      </section>
      <section className="section section-alt">
        <h2 className="section-title">Most Loved Safaris</h2>
        <div className="tours-grid">
          {featured.map(t => <TourCard key={t.id} tour={t} />)}
        </div>
      </section>
    </>
  )
}
