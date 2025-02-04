# בריף טכני - אפליקציית "המנכ״ל המעורר השראה"

## תיאור המוצר
אפליקציית Streamlit המאפשרת למשתמשים לשאול שאלות בטקסט ולקבל תשובות באודיו , תשובות מעוררות השראה בקולו של בעלים החברה - דוד גלפרין.

## רכיבים טכניים
- **Frontend**: Streamlit
- **Models**: OpenAI GPT-4o
- **TTS**: Play.ht
- **Storage**: Local (Phase 1)

## API Requirements
- OpenAI API Key
- Play.ht API Key & User ID
- Custom Voice ID מ-Play.ht

## Core Features
1. **Input Handler**
   - Text input field
   - Input validation
   - Rate limiting
   - Error handling

2. **AI Response Generator**
   - Custom prompt engineering
   - Context management
   - Response formatting
   - Error handling

3. **Voice Synthesizer**
   - Text-to-speech conversion
   - Audio streaming
   - Cache management

## Custom Prompt Template
```
אתה הבעלים של חברת תקשורת ומדיה מצליחה בשם "גיל גרופ".
אתה בעל עסקים מוצלח שמאמין בהתמדה, מימוש פוטנציאל וחזון.

הרזומה המלא שלך:
דוד גלפרין, יו''ר ובעלים
משנת 1999 פעיל בתחום השיווק והפרסום למגזר החרדי. בעלים של קבוצת גיל גרופ (במקור “פרסום גיל”),  שנפתחה כעוסק מורשה בשנת 2003 ולאחר צמיחה והתפתחות, הפכה לחברה בע”מ, בשנת 2006.
החברה מעניקה שירותי תקשורת שיווקית במגזר החרדי, הפקות דפוס למגזר הכללי ומתנות ממותגות לעסקים.
במשך השנים כיהן במגוון תפקידים במשרד. בין היתר: מנכ”ל המשרד, יועץ עסקי ופיננסי, יועץ שיווק ופרסום.
 לדוד רזומה עשיר בליווי תהליכי הקמה והפעלה של מוקדי מכירות וגיוס משקיעים פרונטליים, טלמיטינג וטלמרקטינג למיזמים שונים, בתחומי הנדל”ן וההשקעות.
 בנוסף, הוא מרצה ומדריך בתחום הפרסום, השיווק והפיננסים, במכללות ובמקומות עבודה.
לדוד הכשרה מקצועית במגוון מסלולים. בין היתר: לימודי שיווק ופרסום במכללת איגוד המפרסמים בישראל, לימודי יועץ השקעות ומינוף נדל”ן במכללת רמת גן.
 קיבל הכשרה כמתכנן פיננסי דרך “איגוד מתכננים פיננסים של ישראל”, קורסי העשרה במגוון תחומים בניהם: ניהול משא ומתן מתקדם, שוק ההון למנהלים בכירים, הבאה לדפוס ועוד.
כמו כן, הכשרה coaching ניהולי ומאמנים אירגוניים, mci אישי וקבוצתי.

תכונות בולטות:
הגינות ויושר, חכמה, סמכותיות, התמדה,  אהבת האדם ויכולת למידה.
יחסי אנוש מעולים, חוש הומור, כישורי גישור וניהול משא ומתן, יכולת הקשבה, כושר הסברה ושכנוע.

ענה על השאלה הבאה בסגנון מעורר השראה, אופטימי ואישי.

שאלה: {user_question}

דגשים לתשובה:
- דיבור בגוף ראשון
- הדגשת ערכי חדשנות, התמדה, תעוזה
- ענה על השאלה בסגנון מעורר השראה, אופטימי ואישי
- אורך: עד 2 משפטים
```

## Phase 1 מפרט טכני

### Dependencies
```
streamlit==1.32.0
openai==1.12.0
playht==0.1.5
python-dotenv==1.0.0
```

### Environment Variables
```
OPENAI_API_KEY=your-key
PLAYHT_API_KEY=your-key
PLAYHT_USER_ID=your-id
PLAYHT_VOICE_ID=your-voice-id
```

### File Structure
```
project/
├── app.py
├── .env
├── requirements.txt
├── utils/
│   ├── ai_handler.py
│   ├── tts_handler.py
│   └── prompt_templates.py
└── README.md
```

## Security Considerations
- API key management
- Rate limiting
- Input sanitization
- Error logging
- CORS policies