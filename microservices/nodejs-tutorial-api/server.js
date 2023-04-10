const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors()) // Use this after the variable declaration


// parse requests of content-type - application/json
app.use(express.json());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(express.urlencoded({extended: true}));

// simple route
app.get('/', (req, res) => {
    res.json({message: "Welcome!"});
});


const PORT = process.env.NODE_DOCKER_PORT || 7500;


require("./app/routes/tutorial.routes")(app);
require('./app/routes/auth.routes')(app);
require('./app/routes/user.routes')(app);
require("dotenv").config();

app.listen(PORT, (req, res) => {
    console.log(`Server listening on port ${PORT}. `);
});

const db = require("./app/models");
const Role = db.role;

db.mongoose.connect(db.url, {useNewUrlParser: true, useUnifiedTopology: true})
    .then(() => {
        console.log("Connected to database");
        initial();
    })
    .catch(err => {
        console.log("Error connecting to database : " + err);
        process.exit();
    });

function initial() {
    Role.estimatedDocumentCount((err, count) => {
        if (!err && count === 0) {
            new Role({
                name: "user"
            }).save(err => {
                if (err) {
                    console.log("error", err);
                }

                console.log("added 'user' to roles collection");
            });

            new Role({
                name: "moderator"
            }).save(err => {
                if (err) {
                    console.log("error", err);
                }

                console.log("added 'moderator' to roles collection");
            });

            new Role({
                name: "admin"
            }).save(err => {
                if (err) {
                    console.log("error", err);
                }

                console.log("added 'admin' to roles collection");
            });
        }
    });
}