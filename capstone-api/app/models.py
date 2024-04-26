from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    characters = db.relationship('CharacterSheet', backref='owner', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class CharacterSheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_name = db.Column(db.String(100), nullable=False)
    player_name = db.Column(db.String(100))
    class_level = db.Column(db.String(50))
    background = db.Column(db.String(100))
    race = db.Column(db.String(50))
    alignment = db.Column(db.String(50))
    experience_points = db.Column(db.Integer)
    inspiration = db.Column(db.Boolean)
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    proficiency_bonus = db.Column(db.Integer)
    armor_class = db.Column(db.Integer)
    initiative = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    hit_point_maximum = db.Column(db.Integer)
    current_hit_points = db.Column(db.Integer)
    temporary_hit_points = db.Column(db.Integer)
    hit_dice_total = db.Column(db.String(50))
    hit_dice = db.Column(db.String(50))
    death_save_successes = db.Column(db.Integer)
    death_save_failures = db.Column(db.Integer)
    personality_traits = db.Column(db.Text)
    ideals = db.Column(db.Text)
    bonds = db.Column(db.Text)
    flaws = db.Column(db.Text)
    features_traits = db.Column(db.Text)
    character_backstory = db.Column(db.Text)
    allies_organizations = db.Column(db.Text)
    additional_features_traits = db.Column(db.Text)
    spellcasting_class = db.Column(db.String(100))
    spellcasting_ability = db.Column(db.String(50))
    spell_save_dc = db.Column(db.Integer)
    spell_attack_bonus = db.Column(db.Integer)
    character_appearance = db.Column(db.Text)
    character_image = db.Column(db.String(255))
    faction_symbol_image = db.Column(db.String(255))

    skills = db.relationship('Skill', backref='character_sheet', lazy='dynamic', cascade='all,delete')
    saving_throws = db.relationship('SavingThrow', backref='character_sheet', lazy='dynamic', cascade='all,delete')
    attacks = db.relationship('Attack', backref='character_sheet', lazy='dynamic', cascade='all,delete')
    equipment = db.relationship('Equipment', backref='character_sheet', lazy='dynamic', cascade='all,delete')
    spells = db.relationship('Spell', backref='character_sheet', lazy='dynamic', cascade='all,delete')
    currencies = db.relationship('Currency', backref='character_sheet', lazy='dynamic', cascade='all,delete')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_sheet_id = db.Column(db.Integer, db.ForeignKey('character_sheet.id'), nullable=False)
    skill_name = db.Column(db.String(100))
    is_proficient = db.Column(db.Boolean)
    modifier = db.Column(db.Integer)

class SavingThrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_sheet_id = db.Column(db.Integer, db.ForeignKey('character_sheet.id'), nullable=False)
    save_name = db.Column(db.String(100))
    is_proficient = db.Column(db.Boolean)
    modifier = db.Column(db.Integer)

class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_sheet_id = db.Column(db.Integer, db.ForeignKey('character_sheet.id'), nullable=False)
    name = db.Column(db.String(100))
    attack_bonus = db.Column(db.Integer)
    damage_type = db.Column(db.String(50))

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_sheet_id = db.Column(db.Integer, db.ForeignKey('character_sheet.id'), nullable=False)
    item_name = db.Column(db.String(100))
    item_description = db.Column(db.Text)
    item_image = db.Column(db.String(255))  # URL to image stored in S3

class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_sheet_id = db.Column(db.Integer, db.ForeignKey('character_sheet.id'), nullable=False)
    spell_name = db.Column(db.String(100))
    level = db.Column(db.Integer)
    is_prepared = db.Column(db.Boolean)
    slots_total = db.Column(db.Integer)
    slots_used = db.Column(db.Integer)

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_sheet_id = db.Column(db.Integer, db.ForeignKey('character_sheet.id'), nullable=False)
    cp = db.Column(db.Integer)
    sp = db.Column(db.Integer)
    ep = db.Column(db.Integer)
    gp = db.Column(db.Integer)
    pp = db.Column(db.Integer)
