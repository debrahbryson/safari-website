import { Link } from 'react-router-dom'

export default function TourCard({ tour }) {
  return (
    <div className="tour-card">
      <div className="tour-card-img" style={{ backgroundImage: `url(${tour.image_url})` }}>
        <span className="tour-badge">{tour.duration_days} days</span>
      </div>
      <div className="tour-card-body">
        <div className="tour-meta">
          <span className="tour-park">📍 {tour.park}</span>
          <span className="tour-rating">★ {tour.rating.toFixed(1)}</span>
        </div>
        <h3>{tour.title}</h3>
        <div className="tour-footer">
          <span className="tour-price">from <strong>${tour.price_usd.toLocaleString()}</strong> /person</span>
          <Link to={`/tours/${tour.slug}`} className="btn btn-sm">View →</Link>
        </div>
      </div>
    </div>
  )
}
