const Discord = require('discord.js');
const client = new Discord.Client();
client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
   if (message.content === 'ping') {
     message.reply('pong');
   if (message.content === '%musica') {
     message.content('https://www.youtube.com/watch?v=2HnEud_VRYY');
   }
});

  if (message.content === 'ping') {
     message.reply('pong');
   }

client.login(process.env.BOT_TOKEN);
