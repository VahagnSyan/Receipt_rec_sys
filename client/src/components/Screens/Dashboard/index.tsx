import { Pie } from 'react-chartjs-2';
import { getAnalytics } from '../../../services/authentication';
import { useEffect, useState } from 'react';
import {Chart as ChartJS, Tooltip, Legend, ArcElement} from 'chart.js'
import Loader from '../../Loader/Loader';
ChartJS.register(ArcElement, Tooltip, Legend);

const Dashboard = () => {
    const [data, setData] = useState<any>(null);

    const getUserAnalytics = async () => {
        const analyticsData = await getAnalytics(localStorage.getItem('id')!);

        const categoryPrices = new Map<string, number>();

        analyticsData.forEach((item: any) => {
            const category = item.category;
            const price = parseFloat(item.price);
        
            if (!categoryPrices.has(category)) {
                categoryPrices.set(category, price);
            } else {
                const currentPrice = categoryPrices.get(category)!;
                categoryPrices.set(category, currentPrice + price);
            }
        });
        
        const categories = Array.from(categoryPrices.keys());
        const data = Array.from(categoryPrices.values());
        const chartData = {
            labels: categories,
            datasets: [{
                data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                ],
                borderWidth: 1,
            }],
        };

        setData(chartData);
    };

    useEffect(() => {
        getUserAnalytics();
    }, []);

    if (!data) {
        return <div className='w-full h-[80vh] flex items-center justify-center'><Loader/></div>;
    }

    return (
        <div className='flex items-center justify-center'>
            <Pie data={data} />
        </div>
    );
};

export default Dashboard;