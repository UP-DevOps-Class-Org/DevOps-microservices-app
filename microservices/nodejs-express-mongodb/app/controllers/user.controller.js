exports.allAccess = (request, response) => {
    response.status(200).send("Public Content.");
};

exports.userBoard = (request, response) => {
    response.status(200).send("User Content.");
};

exports.adminBoard = (request, response) => {
    response.status(200).send("Admin Content.");
};

exports.moderatorBoard = (request, response) => {
    response.status(200).send("Moderator Content.");
};