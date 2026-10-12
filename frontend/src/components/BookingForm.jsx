import { useState } from 'react'
import { createBooking } from '../api'

export default function BookingForm({ tour }) {
  const [form, setForm] = useState({
    full_name: '', email: '', phone: '',
    travel_date: '', guests: 2, notes: '',
  })
  const [state, setState] = useState({ loading: false, error: '', success: null })

  const handle = (e) => setForm({ ...form, [e.target.name]: e.target.value })

  const submit = async (e) => {
    e.preventDefault()
    setState({ loading: true, error: '', success: null })
    try {
      const { data } = await createBooking({ ...form, tour_id: tour.id, guests: Number(form.guests) })
      setState({ loading: false, error: '', success: data })
    } catch (err) {
      const msg = err.response?.data?.detail || 'Something went wrong. Please try again.'
      setState({ loading: false, error: Array.isArray(msg) ? msg[0].msg : msg, success: null })
    }
  }

  if (state.success) {
    return (
      <div className="booking-success">
        <h3>✅ Booking Request Received!</h3>
        <p>Reference <strong>#{state.success.id}</strong> — our team will confirm availability
           for <strong>{tour.title}</strong> within 24 hours.</p>
        <p className="muted">A confirmation email is on its way to {state.success.email}.</p>
      </div>
    )
  }

  return (
    <form className="booking-form" onSubmit={submit}>
      <h3>Request This Safari</h3>
      <p className="muted">From <strong>${tour.price_usd.toLocaleString()}</strong> per person · max {tour.max_group_size} guests</p>
      {state.error && <div className="alert alert-error">{state.error}</div>}
      <input name="full_name" placeholder="Full name" required onChange={handle} />
      <input name="email" type="email" placeholder="Email address" required onChange={handle} />
      <input name="phone" placeholder="Phone / WhatsApp" required onChange={handle} />
      <div className="form-row">
        <label>Travel date
          <input name="travel_date" type="date" required onChange={handle} />
        </label>
        <label>Guests
          <input name="guests" type="number" min="1" max={tour.max_group_size}
                 value={form.guests} onChange={handle} />
        </label>
      </div>
      <textarea name="notes" placeholder="Anything we should know? (diet, hotels, special requests)"
                rows="3" onChange={handle} />
      <button className="btn btn-primary btn-block" disabled={state.loading}>
        {state.loading ? 'Sending…' : 'Send Booking Request'}
      </button>
    </form>
  )
}
