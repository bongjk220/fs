package com.ec2.service;

import com.ec2.dto.Movie;
import com.ec2.repository.MovieRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class MovieService {

    private final MovieRepository repo;

    public List<Movie> getAll() {
        return repo.findAll();
    }
}