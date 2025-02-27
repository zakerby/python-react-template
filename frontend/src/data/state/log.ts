import { atom } from 'jotai';

const logAtom = atom([{
    message: "Analysis started",
    timestamp: new Date().toLocaleDateString()
    },
    {
        message: "Fetching repository...",
        timestamp: new Date().toLocaleDateString()
    },
    {
        message: "Ingesting the data in the vector DB, this may take a while...",
        timestamp: new Date().toLocaleDateString()
    },
    {
        message: "Analyzing the data...",
        timestamp: new Date().toLocaleDateString()
    },
    {
        message: "Analysis done.",
        timestamp: new Date().toLocaleDateString()
    }
]);

export {
    logAtom
}