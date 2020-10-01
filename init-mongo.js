db.createUser({
    user: 'zkan',
    pwd: 'zkan',
    roles: [{
        role: 'readWrite',
        db: 'zkan'
    }]
})
