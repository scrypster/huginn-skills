        ---
        name: nestjs-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/nestjs-expert/SKILL.md
        description: Build NestJS services with modules, guards, pipes, and proper DI patterns.
        ---

        You build production NestJS services.

## Module Pattern
```typescript
@Module({
  imports: [TypeOrmModule.forFeature([User])],
  controllers: [UserController],
  providers: [UserService, UserRepository],
  exports: [UserService],
})
export class UserModule {}

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User)
    private readonly users: Repository<User>,
  ) {}

  async create(dto: CreateUserDto): Promise<User> {
    const user = this.users.create(dto)
    return this.users.save(user)
  }
}
```

## Rules
- One module per domain — don't put everything in AppModule.
- Use guards for authentication, pipes for validation, interceptors for logging.
- Use `@nestjs/config` with Joi validation schema for all config.
- Use `@nestjs/testing` with `createTestingModule` for unit tests.
