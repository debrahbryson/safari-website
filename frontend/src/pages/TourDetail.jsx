import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { getTour } from '../api'
import BookingForm from '../components/BookingForm'

export default function TourDetail() {
  const { slug } = useParams()
  const [tour, setTour] = useState(null)
  const [error, setError] = useState('')

  useEffect(() => {
    getTour(slug).then(r => setTour(r.data)).catch(e => setError(e.response?.data?.detail || 'Not found'))
  }, [slug])

  if (error) return <section className="section page"><p className="alert alert-error">{error}</p></section>
  if (!tour) return <section className="section page"><p className="muted">Loading…</p></section>

  return (
    <section className="page">
      <div className="detail-hero" style={{ backgroundImage: `url(${tour.image_url})` }}>
        <div className="hero-overlay" />
        <div className="detail-hero-content">
          <p className="hero-eyebrow">{tour.park}</p>
          <h1>{tour.title}</h1>
          <p>★ {tour.rating.toFixed(1)} · {tour.duration_days} days · max {tour.max_group_size} guests</p>
        </div>
      </div>
      <div className="detail-grid section">
        <div>
          <p className="lead">{tour.description}</p>
          <h3>Highlights</h3>
          <ul className="highlights">
            {tour.highlights.split(',').map((h, i) => <li key={i}>{h.trim()}</li>)}
          </ul>
          <Link to="/tours" className="btn btn-ghost">← All safaris</Link>
        </div>
        <BookingForm tour={tour} />
      </div>
    </section>
  )
}
