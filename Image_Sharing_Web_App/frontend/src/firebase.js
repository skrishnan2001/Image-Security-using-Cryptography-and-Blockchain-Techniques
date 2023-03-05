import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// const firebaseConfig = {
//   apiKey: "AIzaSyBhWAJAq1hkqYzdHOyJ7JdqM80HWT8bJaw",
//   authDomain: "image-sharing-app-c4bfe.firebaseapp.com",
//   projectId: "image-sharing-app-c4bfe",
//   storageBucket: "image-sharing-app-c4bfe.appspot.com",
//   messagingSenderId: "221165350402",
//   appId: "1:221165350402:web:19de4336d9490e3223411b"
// };

// const firebaseConfig = {
//   apiKey: fbConfig.apiKey,
//   authDomain: fbConfig.authDomain,
//   projectId: fbConfig.projectId,
//   storageBucket: fbConfig.storageBucket,
//   messagingSenderId: fbConfig.messagingSenderId,
//   appId: fbConfig.appId
// }

const firebaseConfig = {
  apiKey: process.env.REACT_APP_API_KEY,
  authDomain: process.env.REACT_APP_AUTH_DOMAIN,
  projectId: process.env.REACT_APP_PROJECT_ID,
  storageBucket: process.env.REACT_APP_STORAGE_BUCKET,
  messagingSenderId: process.env.REACT_APP_MESSAGING_SENDER_ID,
  appId: process.env.REACT_APP_APP_ID
}

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export default app;
