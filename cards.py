import random

#shuffle deck
def shuffle_deck(deck):
    random.shuffle(deck)

#pick card
def get_card(deck):
    num = random.randint(0, len(deck)-1)
    card = deck[num]
    del (deck[num])
    rev = random.randint(-1, 1)
    drawn = (card, rev)
    return drawn



#array of dics for cards
def get_deck():
    deck = [
        {"name": "The Magician", "url": "the_magician", "image": "images/Black_02.png", "desc": "The start of something. Beginner’s luck.",
            "message": "Know how to set boundaries", "rdesc": "Trickery, sleight of hand", "cardtype": "major"},

        {"name": "The High Priestess", "url": "the_high_priestess", "image": "images/Black_03.png", "desc": "Wisdom using both intellect and intuition. A spiritual mother.",
            "message": "create a new reality", "rdesc": "Need to hide our true nature behind the conventions of normal society.", "cardtype": "major"},

        {"name": "The Empress", "url": "the_empress", "image": "images/Black_03.png", "desc": "Wisdom using both intellect and intuition. A spiritual mother.",
            "message": "Listen to your guts", "rdesc": "Impulsive behavior. Someone difficult to deal with.", "cardtype": "major"},

        {"name": "The Emperor", "url": "the_emperor", "image": "images/Black_05.png", "desc": "Practical and material achievements.",
            "message": "Leadership and responsibility", "rdesc": "Violence or dictatorship.", "cardtype": "major"},

        {"name": "The Hierophant", "url": "the_hierophant", "image": "images/Black_06.png", "desc": "Teacher or counselor, organized religion or other institution.",
            "message": "respect knowledge and education", "rdesc": "Adherence to outdated norms. Discrimination", "cardtype": "major"},

        {"name": "The Lovers", "url": "the_lovers", "image": "images/Black_07.png", "desc": "Love, relationship or emotional entanglement. A choice",
            "message": "follow your heart", "rdesc": "Tension between several people and hard decisions.", "cardtype": "major"},

        {"name": "The Chariot", "url": "the_chariot", "image": "images/Black_08.png", "desc": "Victory. Motivation to move forward.",
            "message": "do the thing", "rdesc": "Inner weakness hidden behind external show-off.", "cardtype": "major"},

        {"name": "Justice", "url": "justice", "image": "images/Black_12.png", "desc": "Law and order, legal and court issues. A fair and balanced judgment. A developed conscience",
            "message": "act reasonably and do what is expected of you.", "rdesc": "Repressive control of self and of others. Negative ideas blocking change", "cardtype": "major"},

        {"name": "The Hermit", "url": "the_hermit", "image": "images/Black_10.png", "desc": "A quest for truth or for spiritual understanding. Concentrating on a clear purpose.",
            "message": "look for the essence of things", "rdesc": "A closed and reclusive attitude. Isolation, loneliness. Fixed ideas. Excessive caution and suspicion.", "cardtype": "major"},

        {"name": "The Wheel of Fortune", "url": "the_wheel_of_fortune", "image": "images/Black_11.png", "desc": "Change in circumstances and position. A rise after a fall. Gambling, putting faith in capricious luck",
            "message": "accept life's up and downs", "rdesc": "A decline after a period of rising. Running in circles.", "cardtype": "major"},

        {"name": "Strength", "url": "strength", "image": "images/Black_09.png", "desc": "Power and courage to face challenges. Controlled expression of creative urges, drives and desires.",
            "message": "take control of yourself", "rdesc": "The need to keep things under control leads to constant tensions.", "cardtype": "major"},

        {"name": "The Hanged Man", "url": "the_hanged_man", "image": "images/Black_13.png", "desc": "Seeing things from a unique point of view. Enduring difficulties for a worthy cause. A period of deep self examination.",
            "message": "look from a different perspective", "rdesc": "Isolation. Emotional stance of a victim. Inability to act.", "cardtype": "major"},

        {"name": "Temperance", "url": "temperance", "image": "images/Black_14.png", "desc": "Reconciliation, compromise, relaxation of tensions. Ability to do the seemingly impossible.",
            "message": "if there's a will there's a way", "rdesc": "Going back and forth without making real progress.", "cardtype": "major"},

        {"name": "The Devil", "url": "the_devil", "image": "images/Black_17.png", "desc": "A burst of creativity. Paradoxes and contradictions. Irony and mocking of common norms. Acting from desires, passions and impulses.",
            "message": "Express your passion and desires", "rdesc": "Temptation, attraction to the dark and forbidden. Exploitation, egotism, domination.", "cardtype": "major"},

        {"name": "The Tower", "url": "the_tower", "image": "images/Black_16.png", "desc": "Breaking up of solid structures. Getting free from confinement. Sudden breakthrough after long preparations.",
            "message": "return to reality", "rdesc": "Shock, collapse of projects or trusted structures. A fall from an apparently solid and secure position.", "cardtype": "major"},

        {"name": "The Star", "url": "the_star", "image": "images/Black_18.png", "desc": "Openness, simplicity, return to nature. Purity, honesty.",
            "message": "flow from a pure source", "rdesc": "Naive optimism and wishful-thinking. Exposing oneself to danger or abuse.", "cardtype": "major"},

        {"name": "The Moon", "url": "the_moon", "image": "images/Black_19.png", "desc": "Deep emotions, perhaps related to a mother or feminine figure. A different experience of reality. Longing for the unreachable.",
            "message": "don't be afraid to dig deep", "rdesc": "Vague and disturbing feelings. Emotional difficulties, a period of depression.", "cardtype": "major"},

        {"name": "The Sun", "url": "the_sun", "image": "images/Black_20.png", "desc": "Light and warmth, abundance, blessings. Pleasant feeling, emotional or physical healing. Partnership, trust, sharing, brotherhood.",
            "message": "find the right people", "rdesc": "Living in a limited space, difficulty to face reality “in the open.” Immaturity, dependence on others.", "cardtype": "major"},

        {"name": "Judgement", "url": "Judgement", "image": "images/Black_21.png", "desc": "Revelation, enlightenment, a new understanding. A turning point in a therapy process.",
            "message": "spiritual awakening", "rdesc": "Revelation of something that should have been kept hidden. Lack of privacy. Unpleasant realization.", "cardtype": "major"},

        {"name": "The Fool", "url": "the_fool", "image": "images/Black_01.png", "desc": "Freedom from conventions and norms. Something or someone unique and exceptional. Options kept open.",
            "message": "keep moving", "rdesc": "Difficulty in choosing and committing oneself to something stable. Restlessness. Lack of purpose.", "cardtype": "major"},

        {"name": "The World", "url": "the_world", "image": "images/Black_22.png", "desc": "Completion of a process. Balanced activity and achievements in various domains.",
            "message": "everything is perfect as it is", "rdesc": "Life in a bubble, difficulty in sharing your world with others. Disconnection of inner feelings from external life.", "cardtype": "major"},

        {"name": "Death", "url": "death", "image": "images/Black_15.png", "desc": "The end of something whose time has come. Cutting off past influences or attachment to dominant figures.",
            "message": "move on", "rdesc": "Difficulty in coping with loss or change. Temporary difficulties, a trying challenge. Disintegration.", "cardtype": "major"},

        {"name": "King of Swords", "url": "king_of_swords", "image": "images/Black_33.png", "desc": "Determination to break from the past, a strong will.",
            "message": "", "rdesc": "A divided heart, a need to cut off from something to which one is still attached.", "cardtype": "court"},

        {"name": "Queen of Swords", "url": "queen_of_swords", "image": "images/Black_34.png", "desc": "A secure and protected position. Defending one’s territory.",
            "message": "", "rdesc": "Defensiveness and rigidity. Suspicion and fixed ideas block advancement and preclude new connections.", "cardtype": "court"},

        {"name": "Knight of Swords", "url": "knight_of_swords", "image": "images/Black_35.png", "desc": "Energy and resources to advance, still looking for the right direction.",
            "message": "", "rdesc": "Trying to force one’s misguided views, insisting on a wrong direction.", "cardtype": "court"},

        {"name": "Page of Swords", "url": "page_of_swords", "image": "images/Black_36.png", "desc": "Preparation for a future challenge. Looking for a compromise between reason and strong desires.",
            "message": "", "rdesc": "Confusion, negative and inhibiting thoughts, self-defeat.", "cardtype": "court"},

        {"name": "Ace of Swords", "url": "ace_of_swords", "image": "images/Black_23.png", "desc": "A planned initiative. Rational and logical thinking, sharpness of mind. A conclusive decision.",
            "message": "", "rdesc": "Negative and unproductive thoughts. Misconceptions, delusions.", "cardtype": "court"},

        {"name": "Two of Swords", "url": "two_of_swords", "image": "images/Black_24.png", "desc": "Boundaries. Limits that protect and define something which is in development.",
            "message": "", "rdesc": "(similar to upright) Boundaries. Limits that protect and define something which is in development.", "cardtype": "minor"},

        {"name": "Three of Swords", "url": "three_of_swords", "image": "images/Black_25.png", "desc": "Victory. Overcoming a weak opposition. Cutting through a quandary and going forward in a clear direction.",
            "message": "", "rdesc": "A failure, defeat from a weaker opponent. An unsuccessful attempt to make a decisive move.", "cardtype": "minor"},

        {"name": "Four of Swords", "url": "four_of_swords", "image": "images/Black_26.png", "desc": "Restriction. A limited space for development and maneuver. Trying to push against constraints.",
            "message": "", "rdesc": "Confinement and blocking, lack of motivation or energy to break out of a limited situation.", "cardtype": "minor"},

        {"name": "Five of Swords", "url": "five_of_swords", "image": "images/Black_27.png", "desc": "Breakthrough. A forward thrust overcoming the existing limits.",
            "message": "", "rdesc": "A failed initiative to change the situation. Stubbornness leading nowhere.", "cardtype": "minor"},

        {"name": "Six of Swords", "url": "six_of_swords", "image": "images/Black_28.png", "desc": "Adaptation. Accepting limitations and adapting oneself to them. Respecting the present order.",
            "message": "", "rdesc": "Resignation, surrender, giving up the ambition to change things for the better.", "cardtype": "minor"},

        {"name": "Seven of Swords", "url": "seven_of_swords", "image": "images/Black_29.png", "desc": "A focused and determined attitude. Concentrating on a clear goal and doing what it takes to reach it.",
            "message": "", "rdesc": "A narrow and over-concentrated vision. Investing one’s efforts and resources in a lost cause.", "cardtype": "minor"},

        {"name": "Eight of Swords", "url": "eight_of_swords", "image": "images/Black_30.png", "desc": "Defenses. Putting up shields and blocks. Psychological defense mechanisms. A need to be in total control",
            "message": "", "rdesc": "(similar to upright) Defenses. Putting up shields and blocks. Psychological defense mechanisms.", "cardtype": "minor"},

        {"name": "Nine of Swords", "url": "nine_of_swords", "image": "images/Black_31.png", "desc": "Courage. Winning a fight against a superior force. Pure intentions.",
            "message": "", "rdesc": "Losing against a stronger opponent. Sloppiness, imperfect preparations for a challenge.", "cardtype": "minor"},

        {"name": "Ten of Swords", "url": "ten_of_swords", "image": "images/Black_32.png", "desc": "Exhaustion. A complex situation with many conflicting interests. A long battle without a clear outcome.",
            "message": "", "rdesc": "Immobility. Impossible to move now. Feeling attacked from different sides. A painful and humiliating defeat.", "cardtype": "minor"},


        {"name": "King of Pentacles", "url": "king_of_pentacles", "image": "images/Black_61.png", "desc": "Confidence and security, a cautious but optimistic vision. Looking for new achievements while holding existing assets secure",
            "message": "", "rdesc": "Dissatisfaction with what one already has.", "cardtype": "court"},

        {"name": "Queen of Pentacles", "url": "queen_of_pentacles", "image": "images/Black_62.png", "desc": "Tangible assets, material and personal stability, a sober and realistic vision.",
            "message": "", "rdesc": "Conservatism, resistance to change, aiming only to preserve the existing assets.", "cardtype": "court"},

        {"name": "Knight of Pentacles", "url": "knight_of_pentacles", "image": "images/Black_63.png", "desc": "Advancement in a practical direction. A productive expression of creativity.",
            "message": "", "rdesc": "Constant pursuit of money, without reaching material stability", "cardtype": "court"},

        {"name": "Page of Pentacles", "url": "page_of_pentacles", "image": "images/Black_64.png", "desc": "A practical endeavor. Untapped potentials are within reach. Tangible success at the beginning",
            "message": "", "rdesc": "Hesitation, lack of clear purpose.", "cardtype": "court"},

        {"name": "Ace of Pentacles", "url": "ace_of_pentacles", "image": "images/Black_51.png", "desc": "A good start in material things. Financial and physical stability. A practical perspective.",
            "message": "", "rdesc": "(similar to upright) A good start in material things. ", "cardtype": "ace"},

        {"name": "Two of Pentacles", "url": "two_of_pentacles", "image": "images/Black_52.png", "desc": "Duality. Two options or two elements. Collaborating while keeping distance.",
            "message": "", "rdesc": "(similar to upright) Duality. Two options or two elements.", "cardtype": "minor"},

        {"name": "Three of Pentacles", "url": "three_of_pentacles", "image": "images/Black_53.png", "desc": "Product. A partnership or an alliance bears fruit. First results of a project.",
            "message": "", "rdesc": "Disappointment, a partnership or a project does not bear the expected fruits.", "cardtype": "minor"},

        {"name": "Four of Pentacles", "url": "four_of_pentacles", "image": "images/Black_54.png", "desc": "Stability. Solid material assets. Tradition, reputation and honor.",
            "message": "", "rdesc": "Conservatism, clinging to old and outdated patterns.", "cardtype": "minor"},

        {"name": "Five of Pentacles", "url": "five_of_pentacles", "image": "images/Black_55.png", "desc": "Disruption. Something new appears and destabilizes existing structures.",
            "message": "", "rdesc": "(similar to upright) Disruption.", "cardtype": "minor"},

        {"name": "Six of Pentacles", "url": "six_of_pentacles", "image": "images/Black_56.png", "desc": "Expansion. Abundance of resources and possible ways to advance. A positive outlook, success.",
            "message": "", "rdesc": "(similar to upright) Expansion.", "cardtype": "minor"},

        {"name": "Seven of Pentacles", "url": "seven_of_pentacles", "image": "images/Black_57.png", "desc": "Acceptance. Something new is well received. Help and protection.",
            "message": "", "rdesc": "Lack of independence, need to rely on help and acceptance from others.", "cardtype": "minor"},

        {"name": "Eight of Pentacles", "url": "eight_of_pentacles", "image": "images/Black_58.png", "desc": "Uniformity. A mechanical structure. Practical considerations prove efficient, but lack a human touch.",
            "message": "", "rdesc": "(similar to upright) Uniformity. A mechanical structure. Practical considerations prove efficient, but lack a human touch.", "cardtype": "minor"},

        {"name": "Nine of Pentacles", "url": "nine_of_pentacles", "image": "images/Black_59.png", "desc": "Motivation. Carving a niche for oneself in an existing system. Ambition.",
            "message": "", "rdesc": "(similar to upright) Motivation. Carving a niche for oneself in an existing system", "cardtype": "minor"},

        {"name": "Ten of Pentacles", "url": "ten_of_pentacles", "image": "images/Black_60.png", "desc": "Abundance. Intensive activity in practical affairs. Material success and achievements.",
            "message": "", "rdesc": "(similar to upright) Abundance. Intensive activity in practical affairs.", "cardtype": "minor"},


        {"name": "Ace of Wands", "url": "ace_of_wands", "image": "images/Black_65.png", "desc": "Creative momentum. Active sexuality. Strong impulses, energy and drive. Life force.",
            "message": "", "rdesc": "Lack of energy, restriction, repressed sexuality, a creative block.", "cardtype": "ace"},

        {"name": "Two of Wands", "url": "two_of_wands", "image": "images/Black_66.png", "desc": "Crossroads. Several options or ways to choose from. Every course offers benefits.",
            "message": "", "rdesc": "(similar to upright) Crossroads. Several options or ways to choose from. Every course offers benefits.", "cardtype": "minor"},

        {"name": "Three of Wands", "url": "three_of_wands", "image": "images/Black_67.png", "desc": "Direction. Moving forward after a moment of hesitation.",
            "message": "", "rdesc": "(similar to upright) Direction. Moving forward after a moment of hesitation.", "cardtype": "minor"},

        {"name": "Four of Wands", "url": "four_of_wands", "image": "images/Black_68.png", "desc": "Stalemate. A temporary stop in order to prepare for future advancement.",
            "message": "", "rdesc": "(similar to upright) Stalemate. A temporary stop in order to prepare for future advancement.", "cardtype": "minor"},

        {"name": "Five of Wands", "url": "five_of_wands", "image": "images/Black_69.png", "desc": "Overcoming. Getting over a weak opposition. Breakdown of an equilibrium.",
            "message": "", "rdesc": "Walking into a complex situation, losing one’s edge.", "cardtype": "minor"},

        {"name": "Six of Wands", "url": "six_of_wands", "image": "images/Black_70.png", "desc": "Collaboration. A strong alliance between two parties with different goals but common present interests.",
            "message": "", "rdesc": "Excessive pursuit of luxury.", "cardtype": "minor"},

        {"name": "Seven of Wands", "url": "seven_of_wands", "image": "images/Black_71.png", "desc": "Struggle. Someone putting up a fight against many opponents.",
            "message": "", "rdesc": "(similar to upright) Struggle. Someone putting up a fight against many opponents.", "cardtype": "minor"},

        {"name": "Eight of Wands", "url": "eight_of_wands", "image": "images/Black_72.png", "desc": "Regulation. It is possible to advance only by following the rules.",
            "message": "", "rdesc": "(similar to upright) Regulation. It is possible to advance only by following the rules.", "cardtype": "minor"},

        {"name": "Nine of Wands", "url": "nine_of_wands", "image": "images/Black_73.png", "desc": "Interruption. Difficulties and oppositions too hard to overcome",
            "message": "", "rdesc": "(similar to upright) Interruption. Difficulties and oppositions too hard to overcome.", "cardtype": "minor"},

        {"name": "Ten of Wands", "url": "ten_of_wands", "image": "images/Black_74.png", "desc": "Loyalty. A partnership or an alliance endures hardships and succeeds in getting over them.",
            "message": "", "rdesc": "(similar to upright) Loyalty.", "cardtype": "minor"},

        {"name": "King of Wands", "url": "king_of_wands", "image": "images/Black_75.png", "desc": "A mature attitude to urges and desires. Controlled creativity.",
            "message": "", "rdesc": "Plans to move forward are frustrated by self-defeating acts.", "cardtype": "court"},

        {"name": "Queen of Wands", "url": "queen_of_wands", "image": "images/Black_76.png", "desc": "A feminine figure with a strong personality. Things connected with food and eating.",
            "message": "", "rdesc": "Intimidation, menace. Using sexuality as a means of control. Problems with a strong mother figure.", "cardtype": "court"},

        {"name": "Knight of Wands", "url": "knight_of_wands", "image": "images/Black_77.png", "desc": "A change of direction, following one’s urges and passions. A temporary stop.",
            "message": "", "rdesc": "Preoccupation with the satisfaction of one’s own desires. Problem in defining long-term goals.", "cardtype": "court"},

        {"name": "Page of Wands", "url": "page_of_wands", "image": "images/Black_78.png", "desc": "A creative potential which still needs processing.",
            "message": "", "rdesc": "A task too heavy for the querent’s strength. Difficulty in controlling desires and urges.", "cardtype": "court"},


        {"name": "King of Cups", "url": "king_of_cups", "image": "images/Black_47.png", "desc": "Emotional maturity, optimism, ability to overcome past injuries and look ahead.",
            "message": "", "rdesc": "Difficulty in overcoming an emotional blow. A pessimistic outlook caused by negative past experiences.", "cardtype": "court"},

        {"name": "Queen of Cups", "url": "queen_of_cups", "image": "images/Black_48.png", "desc": "A rich inner world which is kept hidden. Guarding one’s privacy or valuable assets.",
            "message": "", "rdesc": "Closure, defensiveness. Distrust of others due to negative past experiences.", "cardtype": "court"},

        {"name": "Knight of Cups", "url": "knight_of_cups", "image": "images/Black_49.png", "desc": "A romantic gesture, offering one’s heart, courting. Openness, sincerity, a simple heart.",
            "message": "", "rdesc": "Superficial and unstable feelings. An over-optimistic but unrealistic attitude.", "cardtype": "court"},

        {"name": "Page of Cups", "url": "page_of_cups", "image": "images/Black_50.png", "desc": "First and unsure steps in a romantic endeavor. Shyness. Sincere intentions.",
            "message": "", "rdesc": "Over-absorption in one’s personal feelings, losing contact with others.", "cardtype": "court"},

        {"name": "Ace of Cups", "url": "ace_of_cups", "image": "images/Black_37.png", "desc": "The beginning of a love relationship. Expression of warm feelings.",
            "message": "", "rdesc": "Emotional dryness, feeling oneself empty", "cardtype": "ace"},

        {"name": "Two of Cups", "url": "two_of_cups", "image": "images/Black_38.png", "desc": "Partnership. A romantic relationship or a close personal alliance.",
            "message": "", "rdesc": "A crisis in a couple relationship, disappointment with someone close to you.", "cardtype": "minor"},

        {"name": "Three of Cups", "url": "three_of_cups", "image": "images/Black_39.png", "desc": "Birth. Something new brings joy and happiness. Caring for a child.",
            "message": "", "rdesc": "Problems in relations with one’s parents, or with one’s child", "cardtype": "minor"},

        {"name": "Four of Cups", "url": "four_of_cups", "image": "images/Black_40.png", "desc": "Family. A collective of people (family, community etc.).",
            "message": "", "rdesc": "Problems and discord in the family or in a long-lasting community.", "cardtype": "minor"},

        {"name": "Five of Cups", "url": "five_of_cups", "image": "images/Black_41.png", "desc": "Links. Popularity, relations with many people. Becoming the center of attention in a group.",
            "message": "", "rdesc": "Excessive preoccupation with social activity.", "cardtype": "minor"},

        {"name": "Six of Cups", "url": "six_of_cups", "image": "images/Black_42.png", "desc": "Continuity. A long-term relationship. Repetition between different generations in the family.",
            "message": "", "rdesc": "Monotony, tedious repetition. Falling time and again into the same emotional traps.", "cardtype": "minor"},

        {"name": "Seven of Cups", "url": "seven_of_cups", "image": "images/Black_43.png", "desc": "Individuality. A single person finding his place in a group. Contact with people in high positions.",
            "message": "", "rdesc": "Problems of integration in a group or an organization.", "cardtype": "minor"},

        {"name": "Eight of Cups", "url": "eight_of_cups", "image": "images/Black_44.png", "desc": "Involvement. Developing personal relationships within a group.",
            "message": "", "rdesc": "Interference of the environment in a couple’s relationships.", "cardtype": "minor"},

        {"name": "Nine of Cups", "url": "nine_of_cups", "image": "images/Black_45.png", "desc": "Collectivity. A group or organization working harmoniously with everyone finding his proper place.",
            "message": "", "rdesc": "A confusing social situation, difficulty in situating oneself within a complex environment.", "cardtype": "minor"},

        {"name": "Ten of Cups", "url": "ten_of_cups", "image": "images/Black_46.png", "desc": "Leadership. A person with special qualities receives appreciation and high status.",
            "message": "", "rdesc": "A fallen leader, loss of popularity. Disappointment because of ingratitude by people one has helped.", "cardtype": "minor"},

    ]
    return deck
