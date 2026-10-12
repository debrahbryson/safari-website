import { useEffect, useState } from 'react'
import TourCard from '../components/TourCard'
import { getTours } from '../api'

export default function Tours() {
  const [tours, setTours] = useState([])
  const [filters, setFilters] = useState({ park: '', max_price: '' })
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(true)
    const params = {}
    if (filters.park) params.park = filters.park
    if (filters.max_price) params.max_price = Number(filters.max_price)
    getTours(params)
      .then(r => setTours(r.data))
      .catch(() => setTours([]))
      .finally(() => setLoading(false))
  }, [filters])

  return (
    <section className="section page">
      <h1 className="section-title">Our Safaris</h1>
      <div className="filters">
        <input placeholder="Search park (e.g. Serengeti)" value={filters.park}
               onChange={e => setFilters({ ...filters, park: e.target.value })} />
        <select value={filters.max_price} onChange={e => setFilters({ ...filters, max_price: e.target.value })}>
          <option value="">Any budget</option>
          <option value="800">Under $800</option>
          <option value="1500">Under $1,500</option>
          <option value="2500">Under $2,500</option>
        </select>
      </div>
      {loading ? <p className="muted">Loading safaris…</p> : (
        tours.length === 0 ? <p className="muted">No safaris match your filters.</p> : (
          <div className="tours-grid">
            {tours.map(t => <TourCard key={t.id} tour={t} />)}
          </div>
        )
      )}
    </section>
  )
}
