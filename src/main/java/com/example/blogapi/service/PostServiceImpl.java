package com.example.blogapi.service;

import com.example.blogapi.entity.Post;
import com.example.blogapi.payload.PostDto;
import com.example.blogapi.repository.PostRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class PostServiceImpl implements PostService {

    @Autowired
    private PostRepository postRepository;

    @Override
    public PostDto createPost(PostDto postDto) {
        Post post = mapToEntity(postDto);
        Post savedPost = postRepository.save(post);
        return mapToDto(savedPost);
    }

    @Override
    public List<PostDto> getAllPosts() {
        List<Post> posts = postRepository.findAll();
        return posts.stream().map(this::mapToDto).collect(Collectors.toList());
    }

    @Override
    public PostDto getPostById(Long id) {
        Post post = postRepository.findById(id).orElse(null);
        return post != null ? mapToDto(post) : null;
    }

    @Override
    public PostDto updatePost(Long id, PostDto postDto) {
    Post existingPost = postRepository.findById(id).orElse(null);
    if (existingPost != null) {
        existingPost.setTitle(postDto.getTitle());
        existingPost.setContent(postDto.getContent());
        existingPost.setAuthor(postDto.getAuthor()); // 👈 Add this too
        Post updatedPost = postRepository.save(existingPost);
        return mapToDto(updatedPost);
    }
    return null;
}


    @Override
    public void deletePost(Long id) {
        postRepository.deleteById(id);
    }

    // Mapping methods
    private PostDto mapToDto(Post post) {
        PostDto dto = new PostDto();
        dto.setId(post.getId());
        dto.setTitle(post.getTitle());
        dto.setContent(post.getContent());
        dto.setAuthor(post.getAuthor()); // 👈 This line was missing
        return dto;
    }
    

    private Post mapToEntity(PostDto dto) {
        Post post = new Post();
        // Don't set the ID for new posts!
        post.setTitle(dto.getTitle());
        post.setContent(dto.getContent());
        post.setAuthor(dto.getAuthor()); // make sure this is mapped too
        return post;
    }
    
}
