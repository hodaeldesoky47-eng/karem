/**
 * English: Custom App to initialize global styles and SWR config.
 * العربية: تطبيق مخصص لتهيئة الأنماط العامة وإعداد SWR.
 */
import type { AppProps } from 'next/app';

export default function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}


