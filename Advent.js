import React, { useState } from 'react';
import { BookOpen, Calendar, ChevronDown, ChevronUp, Star, Sun, Info, Flame, Cross } from 'lucide-react';

const AdventCompanion = () => {
  const [activeTab, setActiveTab] = useState('part1');
  const [expandedDay, setExpandedDay] = useState(null);

  const toggleDay = (id) => {
    if (expandedDay === id) {
      setExpandedDay(null);
    } else {
      setExpandedDay(id);
    }
  };

  const tabs = [
    { id: 'part1', label: 'Part I: True Hope', sub: 'The Messianic Age' },
    { id: 'part2', label: 'Part II: The Forerunner', sub: 'John the Baptist' },
    { id: 'part3', label: 'Part III: The Pre-Nativity', sub: 'Dec 17-24' },
  ];

  const liturgicalNote = `There are two series of readings: one to be used from the beginning of Advent until 16 December; the other from 17 to 24 December. In the last week before Christmas the events that immediately prepared for the Lord's birth are presented.`;

  const readings = {
    part1: [
      {
        id: 'p1-mon1',
        day: '1st Monday',
        title: 'The Faith of a Centurion: Coolest of Israel',
        scripture: 'Matthew 8:5-10',
        context: 'A Roman Centurion asks Jesus to heal his servant but refuses to let Jesus enter his house, citing his own unworthiness.',
        reflection: 'The Centurion is the "coolest" not because of rank, but because he understands the power of Jesus\' Word. He teaches us that hope is universal, not limited to those who think they "belong."',
        lesson: 'Lord, I am not worthy... but only say the word.'
      },
      {
        id: 'p1-tue1',
        day: '1st Tuesday',
        title: 'Be Humble and You\'ll See the Fulfillment of Prophecies',
        scripture: 'Luke 10:21-24',
        context: 'Jesus rejoices that the Father hides mysteries from the "wise" and reveals them to "little children."',
        reflection: 'To see the fulfillment of prophecies, one doesn\'t need a PhD; one needs the open heart of a child. The "wise" rely on intellect; the humble rely on God.',
        lesson: 'We don\'t have to figure everything out. We just have to be small enough to be held by God.'
      },
      {
        id: 'p1-wed1',
        day: '1st Wednesday',
        title: 'A Meal With 4000 Gentiles',
        scripture: 'Matthew 15:29-37',
        context: 'Jesus feeds 4000 people in the Decapolis (Gentile territory) after they had been with Him for three days.',
        reflection: 'The "True Hope" of Advent is Incarnational—God enters our hunger. He is unwilling to send us away hungry.',
        lesson: 'God cares about our physical needs, not just our souls.'
      },
      {
        id: 'p1-thu1',
        day: '1st Thursday',
        title: 'How to Be a Real Disciple with Stone Foundation',
        scripture: 'Matthew 7:21, 24-27',
        context: 'The conclusion of the Sermon on the Mount: building on rock vs. sand.',
        reflection: 'A "Real Disciple" listens and acts. When the rains of life fall, emotional "sand" washes away, but the concrete actions of obedience stand firm.',
        lesson: 'Security is found in what we do in union with God.'
      },
      {
        id: 'p1-fri1',
        day: '1st Friday',
        title: 'Faith Open Eyes',
        scripture: 'Matthew 9:27-31',
        context: 'Two blind men cry out "Son of David" and are healed because of their belief.',
        reflection: 'Their physical sight was restored because their spiritual sight was already active—they recognized Him as Messiah when others did not.',
        lesson: 'We pray to see the world as it really is: charged with God\'s grandeur.'
      },
      {
        id: 'p1-sat1',
        day: '1st Saturday',
        title: 'Jesus Loves the Poor: "Harvest Is Plentiful"',
        scripture: 'Matthew 9:35 - 10:1',
        context: 'Jesus sees the crowds as sheep without a shepherd and empowers the Apostles to help.',
        reflection: 'Jesus organizes a response to suffering. He does not leave us abandoned; He sends laborers (the Church) to heal and help.',
        lesson: 'We are not just waiting for Jesus; He is waiting for us to go to His people.'
      },
      {
        id: 'p1-mon2',
        day: '2nd Monday',
        title: 'Forgiving Sins Is Healing',
        scripture: 'Luke 5:17-26',
        context: 'Jesus forgives the paralyzed man\'s sins before healing his legs.',
        reflection: 'Jesus shows that true healing starts on the inside. He heals the body to prove He can heal the soul.',
        lesson: 'Restoration of the relationship with God is the priority.'
      },
      {
        id: 'p1-tue2',
        day: '2nd Tuesday',
        title: 'Lost Sheep Is Found',
        scripture: 'Matthew 18:12-14',
        context: 'The Shepherd leaves the 99 to find the one lost sheep.',
        reflection: 'The "True Hope" is that God is the pursuer. He risks the 99 for the 1.',
        lesson: 'No matter how lost we feel, the Shepherd is already looking for us.'
      },
      {
        id: 'p1-wed2',
        day: '2nd Wednesday',
        title: 'Tired? Come to Jesus',
        scripture: 'Matthew 11:28-30',
        context: 'Jesus invites the burdened to take His yoke.',
        reflection: 'A yoke couples us to Jesus. We don\'t pull the plow of life alone; He pulls the heavy weight.',
        lesson: 'We find rest IN the work because Christ carries the burden.'
      }
    ],
    part2: [
      {
        id: 'p2-thu2',
        day: '2nd Thursday',
        title: 'Jesus on John: The Greatest Prophet',
        scripture: 'Matthew 11:11-15',
        context: 'Jesus calls John the greatest born of women, yet the least in the Kingdom is greater.',
        reflection: 'John is the greatest of the Old Covenant, but we—the baptized—possess the Spirit in a way he could only point toward.',
        lesson: 'Recognize the immense privilege of living in the age of Grace.'
      },
      {
        id: 'p2-fri2',
        day: '2nd Friday',
        title: 'How John Endured Accusations',
        scripture: 'Matthew 11:16-19',
        context: 'Critics called John possessed because he fasted, and Jesus a glutton because He ate.',
        reflection: 'The world will always find a reason to reject the Gospel. If you are strict, you are crazy; if kind, permissive.',
        lesson: 'We must be true to our mission regardless of public opinion.'
      },
      {
        id: 'p2-sat2',
        day: '2nd Saturday',
        title: 'John is the Returned Elijah',
        scripture: 'Matthew 17:9a, 10-13',
        context: 'Jesus confirms John was the prophesied Elijah, but they killed him.',
        reflection: 'The people missed Elijah because he didn\'t look like their fantasy. They got a man in camel skin instead of a chariot.',
        lesson: 'God rarely comes in the package we expect.'
      },
      {
        id: 'p3-mon3',
        day: '3rd Monday',
        title: 'Authority Questioned',
        scripture: 'Matthew 21:23-27',
        context: 'Pharisees refuse to answer if John\'s baptism was from heaven.',
        reflection: 'They didn\'t care about Truth, only public opinion. You cannot accept Jesus if you reject the repentance John preached.',
        lesson: 'We cannot play politics with God.'
      },
      {
        id: 'p3-tue3',
        day: '3rd Tuesday',
        title: 'The Two Sons',
        scripture: 'Matthew 21:28-32',
        context: 'The son who said "No" but went vs. the son who said "Yes" but didn\'t.',
        reflection: 'Lip service is the enemy. The "bad" people repented; the "religious" people claimed obedience but did nothing.',
        lesson: 'It is better to struggle and obey than to politely agree and ignore.'
      },
      {
        id: 'p3-wed3',
        day: '3rd Wednesday',
        title: 'Tell John Who I Am',
        scripture: 'Luke 7:18b-23',
        context: 'John, in prison, sends disciples to ask if Jesus is the One.',
        reflection: 'Jesus answers John\'s doubt not with arguments, but with miracles. "Look at the fruits."',
        lesson: 'When in doubt, look at where the blind see and the dead rise.'
      },
      {
        id: 'p3-thu3',
        day: '3rd Thursday',
        title: 'John Is More Than a Prophet',
        scripture: 'Luke 7:24-31',
        context: 'Jesus asks if they went to the desert to see a reed shaken by the wind.',
        reflection: 'John was an oak, not a reed. He didn\'t bend to trends. He is the friend of the Bridegroom.',
        lesson: 'Advent calls us to be unshakeable in our values.'
      },
      {
        id: 'p3-fri3',
        day: '3rd Friday',
        title: 'John\'s Testimony is Truth',
        scripture: 'John 5:33-36',
        context: 'Jesus calls John a "burning and shining lamp."',
        reflection: 'John was the Lamp; Jesus is the Sun. The lamp is needed in the dark, but fades when the Sun rises.',
        lesson: 'We are called to be lamps that help others find the Sun.'
      },
       {
        id: 'p3-sat3',
        day: '3rd Saturday',
        title: '[No Reading]',
        scripture: 'Liturgy Note',
        context: 'The Late Advent weekdays (Dec 17-24) take precedence.',
        reflection: 'This marks the shift from John the Baptist to the immediate preparation for the Nativity.',
        lesson: 'We now enter the Octave before Christmas.'
      }
    ],
    part3: [
      {
        id: 'dec17',
        day: 'Dec 17 - O Sapientia',
        title: 'Matthew\'s Prologue: Genealogy',
        scripture: 'Matthew 1:1-17',
        context: 'The 42 generations from Abraham to Jesus.',
        reflection: 'God\'s Wisdom is stronger than human chaos. Jesus\' DNA contains the good, the bad, and the ugly of history.',
        lesson: 'You don\'t have to be perfect to be part of God\'s plan.'
      },
      {
        id: 'dec18',
        day: 'Dec 18 - O Adonai',
        title: 'Joseph: The Foster Dad',
        scripture: 'Matthew 1:18-24',
        context: 'Joseph plans to divorce quietly, but obeys the angel in a dream.',
        reflection: 'Joseph is the silent hero. He speaks no words, but his actions shout. He protects the vulnerability of God.',
        lesson: 'We are guardians of the divine presence in our lives.'
      },
      {
        id: 'dec19',
        day: 'Dec 19 - O Radix',
        title: 'Annunciation to Zechariah',
        scripture: 'Luke 1:5-25',
        specialNote: 'National Resistance Day (Vietnam)',
        context: 'Zechariah is struck mute for doubting God\'s power to give him a son.',
        reflection: 'Just as the Resistance sacrificed all for freedom, Zechariah sacrificed his voice to learn faith. "Better to sacrifice all than lose the nation."',
        lesson: 'When our resources are exhausted, God\'s power begins.'
      },
      {
        id: 'dec20',
        day: 'Dec 20 - O Clavis',
        title: 'Annunciation to Mary',
        scripture: 'Luke 1:26-38',
        context: 'Gabriel visits Mary. She gives her "Fiat."',
        reflection: 'Mary\'s "Yes" is the Key that unlocked Heaven. She does not negotiate; she surrenders.',
        lesson: 'True freedom is found in surrendering to the King.'
      },
      {
        id: 'dec21',
        day: 'Dec 21 - O Oriens',
        title: 'The Visitation',
        scripture: 'Luke 1:39-45',
        context: 'Mary visits Elizabeth; John leaps in the womb.',
        reflection: 'The first Eucharistic procession. John dances like David before the Ark.',
        lesson: 'If we carry Jesus, our presence should make others leap with hope.'
      },
      {
        id: 'dec22',
        day: 'Dec 22 - O Rex',
        title: 'The Magnificat',
        scripture: 'Luke 1:46-56',
        specialNote: 'Vietnamese Armed Forces\' Day',
        context: 'Mary sings that God lifts the lowly and casts down the mighty.',
        reflection: 'Like the 34 soldiers of Gen. Giáp who changed history, Mary proclaims God works through the small. The Magnificat is the anthem of God\'s spiritual army.',
        lesson: 'Do not fear being small; that is where God works.'
      },
      {
        id: 'dec23',
        day: 'Dec 23 - O Emmanuel',
        title: 'Nativity of John the Baptist',
        scripture: 'Luke 1:57-66',
        context: 'John is born; Zechariah writes "His name is John."',
        reflection: 'Naming him John ("God is Gracious") breaks the cycle of tradition. Zechariah\'s tongue is loosed by obedience.',
        lesson: 'We are defined by who God says we are, not our past.'
      },
      {
        id: 'dec24',
        day: 'Dec 24 - Morning',
        title: 'The Benedictus of Zechariah',
        scripture: 'Luke 1:67-79',
        context: 'Zechariah prophesies about the Dawn from on high.',
        reflection: 'The waiting is over. The silence is broken. We stand at the threshold of the Manger.',
        lesson: 'The Dawn is here to guide our feet into the way of peace.'
      }
    ]
  };

  const currentReadings = readings[activeTab];

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 font-sans">
      {/* Hero Header */}
      <div className="bg-purple-900 text-white p-6 shadow-lg">
        <div className="max-w-3xl mx-auto">
          <div className="flex items-center space-x-3 mb-2 opacity-80">
            <Calendar className="w-5 h-5" />
            <span className="text-sm font-semibold tracking-wider uppercase">Liturgical Guide</span>
          </div>
          <h1 className="text-3xl md:text-4xl font-bold mb-2">Advent Weekday Companion</h1>
          <p className="text-purple-200 text-lg italic">"A True Hope"</p>
        </div>
      </div>

      {/* Liturgical Note */}
      <div className="bg-purple-100 border-b border-purple-200 p-4">
        <div className="max-w-3xl mx-auto flex items-start space-x-3 text-purple-900 text-sm">
          <Info className="w-5 h-5 flex-shrink-0 mt-0.5" />
          <p className="italic leading-relaxed">{liturgicalNote}</p>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="sticky top-0 z-10 bg-white shadow-sm border-b border-gray-200 overflow-x-auto">
        <div className="max-w-3xl mx-auto flex">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex-1 py-4 px-2 text-center focus:outline-none transition-colors duration-200 border-b-4 ${
                activeTab === tab.id
                  ? 'border-purple-600 text-purple-900 bg-purple-50'
                  : 'border-transparent text-gray-500 hover:text-purple-600 hover:bg-gray-50'
              }`}
            >
              <div className="font-bold text-sm md:text-base">{tab.label}</div>
              <div className="text-xs font-light hidden md:block">{tab.sub}</div>
            </button>
          ))}
        </div>
      </div>

      {/* Content Area */}
      <div className="max-w-3xl mx-auto p-4 md:p-6 space-y-4">
        {currentReadings.map((reading) => (
          <div 
            key={reading.id} 
            className={`bg-white rounded-xl shadow-sm border transition-all duration-300 overflow-hidden ${
              expandedDay === reading.id ? 'ring-2 ring-purple-500 border-transparent' : 'border-gray-200 hover:border-purple-300'
            }`}
          >
            {/* Card Header */}
            <button
              onClick={() => toggleDay(reading.id)}
              className="w-full text-left p-5 flex items-start justify-between bg-white hover:bg-gray-50 transition-colors"
            >
              <div>
                <div className="flex items-center space-x-2 mb-1">
                  <span className="text-xs font-bold uppercase tracking-wider text-purple-600 bg-purple-100 px-2 py-0.5 rounded">
                    {reading.day}
                  </span>
                  {reading.specialNote && (
                    <span className="text-xs font-bold uppercase tracking-wider text-red-600 bg-red-100 px-2 py-0.5 rounded flex items-center">
                      <Star className="w-3 h-3 mr-1" />
                      Historical Note
                    </span>
                  )}
                </div>
                <h3 className="text-lg font-bold text-gray-900 leading-tight mb-1">{reading.title}</h3>
                <p className="text-sm text-gray-500 font-mono">{reading.scripture}</p>
              </div>
              <div className={`transform transition-transform duration-200 text-purple-400 ${expandedDay === reading.id ? 'rotate-180' : ''}`}>
                <ChevronDown className="w-6 h-6" />
              </div>
            </button>

            {/* Expanded Content */}
            {expandedDay === reading.id && (
              <div className="px-5 pb-6 pt-2 bg-gray-50 border-t border-gray-100 space-y-4 animate-fadeIn">
                
                {/* Special Note Highlight */}
                {reading.specialNote && (
                  <div className="bg-red-50 border-l-4 border-red-500 p-3 rounded-r text-sm text-red-800 mb-4">
                    <strong>Vietnam History:</strong> {reading.specialNote}
                  </div>
                )}

                {/* Context */}
                <div>
                  <h4 className="text-xs font-bold text-gray-400 uppercase tracking-widest mb-1 flex items-center">
                    <BookOpen className="w-3 h-3 mr-1" /> Context
                  </h4>
                  <p className="text-gray-700 leading-relaxed">{reading.context}</p>
                </div>

                {/* Reflection */}
                <div>
                  <h4 className="text-xs font-bold text-gray-400 uppercase tracking-widest mb-1 flex items-center">
                    <Sun className="w-3 h-3 mr-1" /> Reflection
                  </h4>
                  <p className="text-gray-700 leading-relaxed italic border-l-2 border-purple-200 pl-3">
                    "{reading.reflection}"
                  </p>
                </div>

                {/* The Lesson */}
                <div className="bg-purple-600 text-white p-4 rounded-lg shadow-inner mt-4">
                  <h4 className="text-xs font-bold text-purple-200 uppercase tracking-widest mb-2 flex items-center">
                    <Flame className="w-3 h-3 mr-1" /> Advent Lesson
                  </h4>
                  <p className="font-medium text-lg leading-snug">
                    {reading.lesson}
                  </p>
                </div>
              </div>
            )}
          </div>
        ))}

        {/* Footer for the list */}
        <div className="text-center pt-8 pb-12 text-gray-400 text-sm">
          <p>© Advent Weekday Reflections</p>
          <div className="flex justify-center items-center space-x-2 mt-2">
            <Cross className="w-4 h-4" />
            <span>Maranatha, Come Lord Jesus</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdventCompanion;

