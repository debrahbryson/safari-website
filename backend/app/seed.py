from .database import SessionLocal, Base, engine
from .models import Tour

TOURS = [
    dict(title="Great Migration Serengeti Safari", slug="great-migration-serengeti",
         park="Serengeti National Park", duration_days=5, price_usd=1850, rating=4.9,
         image_url="https://images.unsplash.com/photo-1516426122078-c23e76319801",
         description="Follow the wildebeest herds across the endless plains of the Serengeti. "
                     "Witness river crossings, big cats in action and golden savannah sunsets.",
         highlights="Wildebeest river crossings,Big Five game drives,Hot air balloon option,Maasai village visit",
         max_group_size=6),
    dict(title="Ngorongoro Crater Luxury Escape", slug="ngorongoro-crater-luxury",
         park="Ngorongoro Conservation Area", duration_days=3, price_usd=1250, rating=4.8,
         image_url="https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
         description="Descend into the world's largest intact volcanic caldera — a natural amphitheater "
                     "teeming with lions, elephants, rhinos and flamingos.",
         highlights="Black rhino sightings,Crater floor picnic,Lake Magadi flamingos,Lodge on the rim",
         max_group_size=6),
    dict(title="Tarangire Elephant Paradise", slug="tarangire-elephant-paradise",
         park="Tarangire National Park", duration_days=2, price_usd=640, rating=4.7,
         image_url="https://images.unsplash.com/photo-1557050543-4d5f4e07ef46",
         description="Famous for its giant baobab trees and the largest elephant herds in East Africa. "
                     "Perfect short safari from Arusha.",
         highlights="Giant elephant herds,Ancient baobab trees,Silale swamp birding,Sunset game drive",
         max_group_size=8),
    dict(title="Mount Kilimanjaro Lemosho Route", slug="kilimanjaro-lemosho",
         park="Kilimanjaro National Park", duration_days=8, price_usd=2450, rating=4.9,
         image_url="https://images.unsplash.com/photo-1589553416267-fbecb8ff4f7d",
         description="Summit Africa's rooftop via the scenic Lemosho route — the highest success rate "
                     "and the most beautiful approach through rainforest and alpine desert.",
         highlights="Uhuru Peak 5,895m,Professional mountain crew,Full camping gear included,Summit certificate",
         max_group_size=10),
    dict(title="Nyerere (Selous) Wilderness & River", slug="nyerere-selous-wilderness",
         park="Nyerere National Park", duration_days=4, price_usd=1520, rating=4.8,
         image_url="https://images.unsplash.com/photo-1535941339077-2dd1c7963098",
         description="One of Africa's largest reserves — boat safaris on the Rufiji River, walking safaris "
                     "and wild dog encounters far from the crowds.",
         highlights="Rufiji river boat safari,Walking safari with ranger,African wild dogs,Fly-camping option",
         max_group_size=6),
    dict(title="Zanzibar Beach Extension", slug="zanzibar-beach-extension",
         park="Zanzibar Island", duration_days=4, price_usd=890, rating=4.7,
         image_url="https://images.unsplash.com/photo-1580502304784-8985b7eb7260",
         description="Unwind after your safari on powder-white beaches. Spice farm tour, Stone Town "
                     "history and world-class snorkeling at Mnemba Atoll.",
         highlights="Nungwi white-sand beaches,Stone Town walking tour,Spice farm tour,Mnemba snorkeling",
         max_group_size=10),
]

def seed_if_empty():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Tour).count() == 0:
            db.add_all([Tour(**t) for t in TOURS])
            db.commit()
            print(f"Seeded {len(TOURS)} tours")
    finally:
        db.close()
