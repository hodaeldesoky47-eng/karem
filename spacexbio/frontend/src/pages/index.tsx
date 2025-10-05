/**
 * English: Home page for SpaceXBio.
 * العربية: الصفحة الرئيسية لتطبيق SpaceXBio.
 */
import { getApiBaseUrl } from '../lib/api';

export default function Home() {
  return (
    <main style={{ padding: 24 }}>
      <h1>SpaceXBio</h1>
      <p>Welcome. Backend base URL: {getApiBaseUrl()}</p>
    </main>
  );
}


