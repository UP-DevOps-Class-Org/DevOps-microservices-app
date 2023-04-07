const db = require('../models');
const Tutorial = db.tutorials;

const getPagination = (page, size) => {
    const limit = size ? +size : 10;
    const offset = page ? page * limit : 0;

    return {limit, offset};
};

// Create a new tutorial
exports.create = (req, res) => {
    // Validate request
    if (!req.body.title) {
        res.status(400).send({message: "Content can not be empty!"});
        return;
    }

    // Create a Tutorial
    const tutorial = new Tutorial({
        title: req.body.title,
        description: req.body.description,
        published: req.body.published ? req.body.published : false
    });

    // Save Tutorial in the database
    tutorial.save(tutorial).then(data => {
        res.send({message: "Success"});
    }).catch(err => {
        res.status(500).send({
            message: err.message || "Some error occurred while creating the Tutorial."
        });
    });
};

// Retrieve all tutorials

exports.findAll = (request, response) => {
    const {page, size, title} = request.query;
    let condition = title ? {title: {$regex: new RegExp(title), $options: "i"}} : {};

    const {limit, offset} = getPagination(page, size);

    const options = {
        offset: offset,
        limit: limit,
        collation: {   // <--- setup the sorting options via the collation flags
            locale: 'en',

        },
        sort: {date: -1}
    };

    Tutorial.paginate(condition, options)
        .then(data => {
            response.send({
                totalItem: data.totalDocs,
                data: data.docs,
                totalPages: data.totalPages,
                currentPage: data.page - 1,
            });
            // data.docs.sort().reverse(); // sort by latest added

        })
        .catch(err => {
            response.status(500).send({
                code: err.code,
                message: err.message || "Some error occurred while retrieving tutorials."
            });
        });
};

// Find a single Tutorial with an id
exports.findOne = (req, res) => {

    const id = req.params.id;

    Tutorial.findById(id).then(data => {
        if (!data) {
            res.status(404).send({message: "Not found Tutorial with id " + id});
        } else res.send({data: data});
    }).catch(err => {
        res.status(500).send({message: "Error retrieving Tutorial with id=" + id});
    });
};

// Update a Tutorial by the id in the request
exports.update = (request, response) => {
    if (!request.body) {
        return request.status(404).send({message: "Data to update can not be empty!"});
    }

    const id = request.params.id;

    Tutorial.findByIdAndUpdate(id, request.body, {useFindAndModify: false})
        .then(data => {
            if (!data) {
                response.status(404).send({message: `Cannot update Tutorial with id=${id}. Maybe Tutorial was not found!`})
            } else response.send({message: "Tutorial was updated successfully."});
        })
        .catch(err => {
            response.status(500).send({message: "Error updating Tutorial with id=" + id});
        });
};

// Delete a Tutorial with the specified id in the request
exports.delete = (request, response) => {

    const id = request.params.id;
    Tutorial.findByIdAndRemove(id)
        .then(data => {
            if (!data) {
                return request.status(404).send({message: `Cannot delete Tutorial with id=${id}. Maybe Tutorial was not found!`})
            } else response.send({message: "Tutorial was deleted successfully!"})
        })
        .catch(err => {
            return response.status(500).send({message: err.message || "Could not delete Tutorial with id=" + id})
        });
};

// Delete all Tutorials from the database.
exports.deleteAll = (request, response) => {
    Tutorial.deleteMany({})
        .then(data => {
            response.send({message: `${data.deletedCount} Tutorials were deleted successfully!`});
        })
        .catch(err => {
            response.status(500).send({message: err.message || "Some error occurred while removing all tutorials."})
        });
};

// Find all published Tutorials
exports.findAllPublished = (req, res) => {
    Tutorial.find({published: true})
        .then(data => {
            res.send({data: data});
        })
        .catch(err => {
            res.status(500).send({
                message: err.message || "Some error occurred while retrieving tutorials."
            });
        });

};