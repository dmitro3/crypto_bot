import { RootState } from '@/store';
import { FC, useEffect, useRef } from 'react';
import { useSelector } from 'react-redux';
import styles from './chart.module.css';

interface ChartProps {
  mode: 'candleStick' | 'line';
  symbol: string;
}

const createScales = (count: number, className: string) => {
  return Array.from({ length: count }).map((_, index) => (
    <div key={index} className={className}></div>
  ));
};

const Chart: FC<ChartProps> = ({ mode, symbol }) => {
  const { chartTime } = useSelector((state: RootState) => state.chart);
  const container = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Clear any previous chart to prevent duplication
    if (container.current) {
      container.current.innerHTML = '';
    }

    // Create the TradingView chart script
    const script = document.createElement('script');
    script.src =
      'https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js';
    script.type = 'text/javascript';
    script.async = true;
    script.innerHTML = `
      {
        "autosize": "true",
        "symbol": "${symbol}",
        "interval": "${chartTime}",
        "timezone": "Etc/UTC",
        "theme": "dark",
        "style": "${mode === 'candleStick' ? '1' : '2'}",
        "locale": "en",
        "hide_top_toolbar": true,
        "hide_legend": true,
        "allow_symbol_change": false,
        "save_image": false,
        "calendar": false,
        "hide_volume": true,
        "support_host": "https://www.tradingview.com"
      }`;

    container.current?.appendChild(script);
  }, [mode, symbol, chartTime]);

  return (
    <div
      className={`${styles['tradingview-widget-container']} ${styles.chartContainer}`}
      ref={container}
    >
      <div className="tradingview-widget-container__widget"></div>
    </div>
  );
};

export default Chart;
